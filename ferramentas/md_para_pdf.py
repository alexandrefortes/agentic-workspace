#!/usr/bin/env python3
"""
Script de Conversão: Markdown → PDF
Converte documentos Markdown para PDF com qualidade profissional.

Uso:
    python md_para_pdf.py documento.md
    python md_para_pdf.py documento.md --assinavel
    python md_para_pdf.py documento.md --marca-dagua "CONFIDENCIAL"
"""

import argparse
import subprocess
import sys
from pathlib import Path
from datetime import datetime
import re

# Configurações
LOG_DIR = Path("../logs")
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


def converter_para_pdf(arquivo_md, arquivo_saida=None, assinavel=False, marca_dagua=None):
    """
    Converte arquivo Markdown para PDF usando Pandoc + LaTeX.
    
    Args:
        arquivo_md: Caminho do arquivo Markdown
        arquivo_saida: Caminho do arquivo PDF de saída (opcional)
        assinavel: Se True, gera PDF otimizado para assinatura digital
        marca_dagua: Texto da marca d'água (opcional)
    
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
    
    if assinavel:
        print(f"✍️  Modo: PDF assinável")
    if marca_dagua:
        print(f"🔒 Marca d'água: {marca_dagua}")
    
    # Ler e sanitizar conteúdo
    try:
        with open(arquivo_md, 'r', encoding='utf-8') as f:
            conteudo = f.read()
        
        conteudo_limpo = sanitizar_markdown(conteudo)
        
        # Adicionar marca d'água se solicitado
        if marca_dagua:
            # Adicionar comando LaTeX para marca d'água no cabeçalho
            header_latex = f"""
---
header-includes: |
  \\usepackage{{draftwatermark}}
  \\SetWatermarkText{{{marca_dagua}}}
  \\SetWatermarkScale{{0.5}}
  \\SetWatermarkColor[gray]{{0.9}}
---

"""
            conteudo_limpo = header_latex + conteudo_limpo
        
        # Criar arquivo temporário com conteúdo sanitizado
        arquivo_temp = arquivo_md.with_suffix('.temp.md')
        with open(arquivo_temp, 'w', encoding='utf-8') as f:
            f.write(conteudo_limpo)
        
    except Exception as e:
        print(f"❌ Erro ao ler arquivo: {e}")
        registrar_log(arquivo_md, arquivo_saida, "ERRO", f"Erro ao ler: {e}")
        return False
    
    # Construir comando Pandoc
    cmd = [
        'pandoc',
        str(arquivo_temp),
        '-o', str(arquivo_saida),
        '--pdf-engine=xelatex',
        '--standalone',
        '-V', 'geometry:margin=2.5cm',
        '-V', 'fontsize=11pt',
        '-V', 'papersize=a4',
    ]
    
    # Opções para PDF assinável
    if assinavel:
        cmd.extend([
            '-V', 'colorlinks=true',
            '-V', 'linkcolor=blue',
            '-V', 'urlcolor=blue',
        ])
    
    # Executar conversão
    try:
        print("⏳ Convertendo... (pode demorar na primeira vez)")
        
        resultado = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace',  # Substituir caracteres inválidos
            check=True
        )
        
        # Limpar arquivo temporário
        arquivo_temp.unlink()
        
        print(f"✅ Conversão concluída com sucesso!")
        print(f"📊 Tamanho: {arquivo_saida.stat().st_size / 1024:.1f} KB")
        
        opcoes = []
        if assinavel:
            opcoes.append("assinável")
        if marca_dagua:
            opcoes.append(f"marca d'água: {marca_dagua}")
        
        registrar_log(
            arquivo_md,
            arquivo_saida,
            "SUCESSO",
            ", ".join(opcoes) if opcoes else "padrão"
        )
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
        
        registrar_log(arquivo_md, arquivo_saida, "ERRO", f"Pandoc: {e.stderr[:100]}")
        return False
    
    except FileNotFoundError:
        print(f"❌ Erro: Pandoc não encontrado!")
        print(f"   Instale com: winget install --id JohnMacFarlane.Pandoc")
        
        # Limpar arquivo temporário
        if arquivo_temp.exists():
            arquivo_temp.unlink()
        
        registrar_log(arquivo_md, arquivo_saida, "ERRO", "Pandoc não instalado")
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Converte Markdown para PDF com qualidade profissional',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  python md_para_pdf.py documento.md
  python md_para_pdf.py documento.md --assinavel
  python md_para_pdf.py documento.md --marca-dagua "CONFIDENCIAL"
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
    
    parser.add_argument(
        '--assinavel',
        action='store_true',
        help='Gera PDF otimizado para assinatura digital'
    )
    
    parser.add_argument(
        '--marca-dagua',
        help='Adiciona marca d\'água ao PDF (ex: "CONFIDENCIAL", "RASCUNHO")'
    )
    
    args = parser.parse_args()
    
    # Executar conversão
    sucesso = converter_para_pdf(
        args.arquivo,
        args.output,
        args.assinavel,
        args.marca_dagua
    )
    
    sys.exit(0 if sucesso else 1)


if __name__ == '__main__':
    main()
