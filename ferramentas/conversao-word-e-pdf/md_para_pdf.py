#!/usr/bin/env python3
"""
Script de Conversão: Markdown → PDF
Converte documentos Markdown para PDF com qualidade profissional.

Uso:
    python md_para_pdf.py documento.md
    python md_para_pdf.py documento.md --output saida/documento.pdf
"""

import argparse
import subprocess
import sys
import io
from pathlib import Path
from datetime import datetime
import re

# Configurar stdout para UTF-8 no Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Configurações
LOG_DIR = Path("./logs")
LOG_DIR.mkdir(exist_ok=True)


def sanitizar_markdown(conteudo):
    """
    Remove tags perigosas do Markdown para mitigar vulnerabilidades do Pandoc.
    
    Remove:
    - Tags <iframe>
    - Tags <script>
    - Tags <object>
    - Tags <embed>
    """
    padroes_perigosos = [
        r'<iframe[^>]*>.*?</iframe>',
        r'<script[^>]*>.*?</script>',
        r'<object[^>]*>.*?</object>',
        r'<embed[^>]*>.*?</embed>',
        r'<iframe[^>]*/>',
        r'<script[^>]*/>',
        r'<object[^>]*/>',
        r'<embed[^>]*/>',
        # Remove SVG badges (fix for missing rsvg-convert)
        r'!\[[^\]]*\]\([^)]*(?:\.svg|shields\.io|badge)[^)]*\)',
    ]
    
    conteudo_limpo = conteudo
    tags_removidas = []
    
    for padrao in padroes_perigosos:
        matches = re.findall(padrao, conteudo_limpo, re.IGNORECASE | re.DOTALL)
        if matches:
            tags_removidas.extend(matches)
            conteudo_limpo = re.sub(padrao, '', conteudo_limpo, flags=re.IGNORECASE | re.DOTALL)
    
    if tags_removidas:
        print(f"⚠️  AVISO: {len(tags_removidas)} tag(s) perigosa(s) removida(s) por segurança:")
        for tag in tags_removidas[:3]:
            print(f"   - {tag[:50]}...")
    
    return conteudo_limpo


def registrar_log(arquivo_entrada, arquivo_saida, status, mensagem=""):
    """Registra operação no log de auditoria."""
    log_file = LOG_DIR / f"{datetime.now().strftime('%Y-%m-%d')}-conversoes.log"
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    usuario = "sistema"
    
    linha_log = f"{timestamp} | {usuario} | md_para_pdf.py | {arquivo_entrada} → {arquivo_saida} | {status}"
    if mensagem:
        linha_log += f" | {mensagem}"
    
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(linha_log + '\n')


def converter_para_pdf(arquivo_md, arquivo_saida=None):
    """
    Converte arquivo Markdown para PDF usando Pandoc + LaTeX.
    
    Args:
        arquivo_md: Caminho do arquivo Markdown
        arquivo_saida: Caminho do arquivo PDF de saída (opcional)
    
    Returns:
        True se conversão foi bem-sucedida, False caso contrário
    """
    arquivo_md = Path(arquivo_md)
    
    # Validar arquivo de entrada
    if not arquivo_md.exists():
        print(f"❌ Erro: Arquivo não encontrado: {arquivo_md}")
        registrar_log(arquivo_md, "N/A", "ERRO", "Arquivo não encontrado")
        return False
    
    # Definir arquivo de saída
    if arquivo_saida is None:
        arquivo_saida = arquivo_md.with_suffix('.pdf')
    else:
        arquivo_saida = Path(arquivo_saida)
    
    # Criar diretório de saída se não existir
    arquivo_saida.parent.mkdir(parents=True, exist_ok=True)
    
    print(f"📄 Convertendo: {arquivo_md.name}")
    print(f"📁 Saída: {arquivo_saida}")
    
    # Ler e sanitizar conteúdo
    try:
        with open(arquivo_md, 'r', encoding='utf-8') as f:
            conteudo = f.read()
        
        conteudo_limpo = sanitizar_markdown(conteudo)
        
        # Criar arquivo temporário com conteúdo sanitizado
        arquivo_temp = arquivo_md.with_suffix('.temp.md')
        with open(arquivo_temp, 'w', encoding='utf-8') as f:
            f.write(conteudo_limpo)
            
        # Criar arquivo de header LaTeX temporário para quebra de linha em código
        header_content = r'''
\usepackage{fvextra}
\fvset{breaklines}
        '''
        header_temp = arquivo_md.with_suffix('.header.tex')
        with open(header_temp, 'w', encoding='utf-8') as f:
            f.write(header_content)
        
    except Exception as e:
        print(f"❌ Erro ao ler/criar arquivos: {e}")
        registrar_log(arquivo_md, arquivo_saida, "ERRO", f"Erro IO: {e}")
        return False
    
    # Construir comando Pandoc
    cmd = [
        'pandoc',
        str(arquivo_temp),
        '-o', str(arquivo_saida),
        '--pdf-engine=xelatex',
        '--standalone',
        '-H', str(header_temp),
        '-V', 'geometry:margin=2.5cm',
        '-V', 'fontsize=11pt',
        '-V', 'papersize=a4',
    ]
    
    # Executar conversão
    try:
        print("⏳ Convertendo... (pode demorar na primeira vez)")
        
        resultado = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace',
            check=True
        )
        
        # Limpar arquivos temporários
        arquivo_temp.unlink()
        header_temp.unlink()
        
        print(f"✅ Conversão concluída com sucesso!")
        print(f"📊 Tamanho: {arquivo_saida.stat().st_size / 1024:.1f} KB")
        
        registrar_log(arquivo_md, arquivo_saida, "SUCESSO")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro na conversão:")
        print(f"   {e.stderr}")
        
        # Verificar se é erro de LaTeX não instalado
        if "xelatex not found" in e.stderr.lower() or "pdflatex" in e.stderr.lower():
            print(f"\n💡 Dica: Instale o MiKTeX para gerar PDFs:")
            print(f"   winget install MiKTeX.MiKTeX")
        
        # Limpar arquivo temporário
        if arquivo_temp.exists():
            arquivo_temp.unlink()
        if header_temp.exists():
            header_temp.unlink()
        
        registrar_log(arquivo_md, arquivo_saida, "ERRO", f"Pandoc: {e.stderr[:100]}")
        return False
    
    except FileNotFoundError:
        print(f"❌ Erro: Pandoc não encontrado!")
        print(f"   Instale com: winget install --id JohnMacFarlane.Pandoc")
        
        # Limpar arquivo temporário
        if arquivo_temp.exists():
            arquivo_temp.unlink()
        if header_temp.exists():
            header_temp.unlink()
        
        registrar_log(arquivo_md, arquivo_saida, "ERRO", "Pandoc não instalado")
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Converte Markdown para PDF com qualidade profissional',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  python md_para_pdf.py documento.md
  python md_para_pdf.py documento.md --output saida/documento.pdf
  
Requisitos:
  - Pandoc (winget install --id JohnMacFarlane.Pandoc)
  - MiKTeX (winget install MiKTeX.MiKTeX)
        """
    )
    
    parser.add_argument(
        'arquivo',
        help='Arquivo Markdown para converter'
    )
    
    parser.add_argument(
        '--output', '-o',
        help='Arquivo PDF de saída (padrão: mesmo nome com .pdf)'
    )
    
    args = parser.parse_args()
    
    # Executar conversão
    sucesso = converter_para_pdf(
        args.arquivo,
        args.output
    )
    
    sys.exit(0 if sucesso else 1)


if __name__ == '__main__':
    main()
