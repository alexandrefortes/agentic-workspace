#!/usr/bin/env python3
"""
Script de Conversão: Markdown → Word
Converte documentos Markdown para Word (.docx) com segurança e templates corporativos.

Uso:
    python md_para_word.py documento.md
    python md_para_word.py documento.md --template juridico
    python md_para_word.py documento.md --output saida/documento.docx
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
TEMPLATES_DIR = Path("../templates")
LOG_DIR = Path("./logs")
LOG_DIR.mkdir(exist_ok=True)

# Templates disponíveis por área
TEMPLATES = {
    "juridico": TEMPLATES_DIR / "contrato-base.docx",
    "rh": TEMPLATES_DIR / "politica-base.docx",
    "compliance": TEMPLATES_DIR / "relatorio-base.docx",
    "comercial": TEMPLATES_DIR / "proposta-base.docx",
}


def sanitizar_markdown(conteudo):
    """
    Remove tags perigosas do Markdown para mitigar vulnerabilidades do Pandoc.
    
    Remove:
    - Tags <iframe>
    - Tags <script>
    - Tags <object>
    - Tags <embed>
    """
    # Padrões perigosos
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
        for tag in tags_removidas[:3]:  # Mostrar apenas as 3 primeiras
            print(f"   - {tag[:50]}...")
    
    return conteudo_limpo


def registrar_log(arquivo_entrada, arquivo_saida, status, mensagem=""):
    """Registra operação no log de auditoria."""
    log_file = LOG_DIR / f"{datetime.now().strftime('%Y-%m-%d')}-conversoes.log"
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    usuario = "sistema"  # Em produção, pegar do ambiente
    
    linha_log = f"{timestamp} | {usuario} | md_para_word.py | {arquivo_entrada} → {arquivo_saida} | {status}"
    if mensagem:
        linha_log += f" | {mensagem}"
    
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(linha_log + '\n')


def converter_para_word(arquivo_md, arquivo_saida=None, template=None):
    """
    Converte arquivo Markdown para Word usando Pandoc.
    
    Args:
        arquivo_md: Caminho do arquivo Markdown
        arquivo_saida: Caminho do arquivo Word de saída (opcional)
        template: Nome do template a usar (juridico, rh, compliance, comercial)
    
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
        arquivo_saida = arquivo_md.with_suffix('.docx')
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
        
    except Exception as e:
        print(f"❌ Erro ao ler arquivo: {e}")
        registrar_log(arquivo_md, arquivo_saida, "ERRO", f"Erro ao ler: {e}")
        return False
    
    # Construir comando Pandoc
    cmd = [
        'pandoc',
        str(arquivo_temp),
        '-o', str(arquivo_saida),
        '--standalone',
    ]
    
    # Adicionar template se especificado
    if template:
        if template in TEMPLATES:
            template_path = TEMPLATES[template]
            if template_path.exists():
                cmd.extend(['--reference-doc', str(template_path)])
                print(f"📋 Usando template: {template}")
            else:
                print(f"⚠️  Aviso: Template '{template}' não encontrado, usando padrão")
        else:
            print(f"⚠️  Aviso: Template '{template}' desconhecido, usando padrão")
            print(f"   Templates disponíveis: {', '.join(TEMPLATES.keys())}")
    
    # Executar conversão
    try:
        resultado = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        
        # Limpar arquivo temporário
        arquivo_temp.unlink()
        
        print(f"✅ Conversão concluída com sucesso!")
        print(f"📊 Tamanho: {arquivo_saida.stat().st_size / 1024:.1f} KB")
        
        registrar_log(arquivo_md, arquivo_saida, "SUCESSO", f"Template: {template or 'padrão'}")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro na conversão:")
        print(f"   {e.stderr}")
        
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
        description='Converte Markdown para Word com segurança e templates corporativos',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  python md_para_word.py documento.md
  python md_para_word.py documento.md --template juridico
  python md_para_word.py documento.md --output saida/documento.docx
  
Templates disponíveis:
  juridico   - Contratos e documentos legais
  rh         - Políticas e comunicados
  compliance - Relatórios de auditoria
  comercial  - Propostas e apresentações
        """
    )
    
    parser.add_argument(
        'arquivo',
        help='Arquivo Markdown para converter'
    )
    
    parser.add_argument(
        '--output', '-o',
        help='Arquivo Word de saída (padrão: mesmo nome com .docx)'
    )
    
    parser.add_argument(
        '--template', '-t',
        choices=list(TEMPLATES.keys()),
        help='Template corporativo a usar'
    )
    
    args = parser.parse_args()
    
    # Executar conversão
    sucesso = converter_para_word(
        args.arquivo,
        args.output,
        args.template
    )
    
    sys.exit(0 if sucesso else 1)


if __name__ == '__main__':
    main()
