# 🔧 Ferramentas de Conversão

Scripts Python para converter documentos Markdown em formatos corporativos (Word e PDF) com segurança e qualidade profissional.

---

## 📋 Scripts Disponíveis

### 1. `md_para_word.py` - Conversão para Word

Converte Markdown para Word (.docx) com sanitização de segurança e templates corporativos.

**Uso básico:**
```bash
python md_para_word.py documento.md
```

**Com template:**
```bash
python md_para_word.py documento.md --template juridico
```

**Especificar saída:**
```bash
python md_para_word.py documento.md --output saida/documento.docx
```

**Templates disponíveis:**
- `juridico` - Contratos e documentos legais
- `rh` - Políticas e comunicados
- `compliance` - Relatórios de auditoria
- `comercial` - Propostas e apresentações

---

### 2. `md_para_pdf.py` - Conversão para PDF

Converte Markdown para PDF com qualidade profissional usando LaTeX.

**Uso básico:**
```bash
python md_para_pdf.py documento.md
```

**PDF assinável:**
```bash
python md_para_pdf.py documento.md --assinavel
```

**Com marca d'água:**
```bash
python md_para_pdf.py documento.md --marca-dagua "CONFIDENCIAL"
```

**Especificar saída:**
```bash
python md_para_pdf.py documento.md --output saida/documento.pdf
```

---

## 🔒 Segurança

Ambos os scripts implementam **sanitização automática** para mitigar vulnerabilidades do Pandoc:

### Tags Removidas Automaticamente
- `<iframe>` - Previne SSRF (CVE-2025-51591)
- `<script>` - Previne execução de código
- `<object>` - Previne injeção de objetos
- `<embed>` - Previne incorporação maliciosa

### Exemplo de Sanitização
```markdown
# Documento Original
Texto normal
<iframe src="http://169.254.169.254/latest/meta-data/"></iframe>
Mais texto

# Após Sanitização
Texto normal

Mais texto
```

O script avisa quando tags são removidas:
```
⚠️  AVISO: 1 tag(s) perigosa(s) removida(s) por segurança:
   - <iframe src="http://169.254.169.254/latest/...
```

---

## 📊 Logs de Auditoria

Todas as conversões são registradas automaticamente em:
```
../logs/AAAA-MM-DD-conversoes.log
```

**Formato do log:**
```
2026-01-24 14:30:15 | usuario@empresa.com | md_para_word.py | documento.md → documento.docx | SUCESSO | Template: juridico
2026-01-24 14:31:22 | usuario@empresa.com | md_para_pdf.py | documento.md → documento.pdf | SUCESSO | assinável
```

**Informações registradas:**
- Data e hora
- Usuário (em produção)
- Script usado
- Arquivos de entrada e saída
- Status (SUCESSO/ERRO)
- Opções usadas

---

## 🚀 Instalação

### 1. Instalar Python
```bash
winget install Python.Python.3.12
```

### 2. Instalar Pandoc
```bash
winget install --id JohnMacFarlane.Pandoc
```

### 3. Instalar MiKTeX (para PDFs)
```bash
winget install MiKTeX.MiKTeX
```

### 4. Verificar Instalação
```bash
python --version
pandoc --version
xelatex --version
```

---

## 🧪 Testes

### Teste Rápido - Word
```bash
# Criar arquivo de teste
echo "# Teste\n\nEste é um teste." > teste.md

# Converter
python md_para_word.py teste.md

# Verificar
dir teste.docx
```

### Teste Rápido - PDF
```bash
# Criar arquivo de teste
echo "# Teste\n\nEste é um teste." > teste.md

# Converter
python md_para_pdf.py teste.md

# Verificar
dir teste.pdf
```

### Teste de Segurança
```bash
# Criar arquivo com tag perigosa
echo "# Teste\n\n<iframe src='http://malicious.com'></iframe>" > teste-seguranca.md

# Converter (deve remover o iframe)
python md_para_word.py teste-seguranca.md

# Verificar aviso de segurança no console
```

---

## ⚙️ Opções Avançadas

### Conversão em Lote
```bash
# Converter todos os .md de uma pasta
for %f in (*.md) do python md_para_word.py %f
```

### Integração com Kiro
Os scripts podem ser chamados diretamente pelo Kiro via steering files:

```markdown
# No steering file
Após gerar o documento, execute:
python ferramentas/md_para_word.py documento.md --template juridico
python ferramentas/md_para_pdf.py documento.md --assinavel
```

---

## 🐛 Troubleshooting

### Problema 1: "Pandoc não encontrado"

**Sintoma:**
```
❌ Erro: Pandoc não encontrado!
   Instale com: winget install --id JohnMacFarlane.Pandoc
```

**Causa:** Pandoc não está instalado ou não está no PATH do sistema.

**Solução:**

1. **Instalar Pandoc:**
```bash
winget install --id JohnMacFarlane.Pandoc
```

2. **Verificar instalação:**
```bash
pandoc --version
```

3. **Se ainda não funcionar, adicionar ao PATH manualmente:**

Pandoc geralmente é instalado em:
- `C:\Users\[seu-usuario]\AppData\Local\Pandoc\`
- `C:\Program Files\Pandoc\`

**Adicionar ao PATH temporariamente (PowerShell):**
```powershell
$env:PATH += ";$env:LOCALAPPDATA\Pandoc"
```

**Adicionar ao PATH permanentemente:**
1. Abrir "Variáveis de Ambiente" no Windows
2. Editar variável PATH do usuário
3. Adicionar: `C:\Users\[seu-usuario]\AppData\Local\Pandoc`
4. Reiniciar terminal

---

### Problema 2: "xelatex not found" (PDF)

**Sintoma:**
```
❌ Erro na conversão:
   xelatex not found
   
💡 Dica: Instale o MiKTeX para gerar PDFs:
   winget install MiKTeX.MiKTeX
```

**Causa:** MiKTeX (LaTeX) não está instalado ou não está no PATH.

**Solução:**

1. **Instalar MiKTeX:**
```bash
winget install MiKTeX.MiKTeX
```

2. **Verificar instalação:**
```bash
xelatex --version
```

3. **Se ainda não funcionar, adicionar ao PATH:**

MiKTeX geralmente é instalado em:
- `C:\Program Files\MiKTeX\miktex\bin\x64\`
- `C:\Users\[seu-usuario]\AppData\Local\Programs\MiKTeX\miktex\bin\x64\`

**Adicionar ao PATH temporariamente (PowerShell):**
```powershell
$env:PATH += ";C:\Program Files\MiKTeX\miktex\bin\x64"
```

---

### Problema 3: Conversão PDF muito lenta na primeira vez

**Sintoma:**
```
⏳ Convertendo... (pode demorar na primeira vez)
[Aguardando 2-3 minutos...]
```

**Causa:** MiKTeX está baixando pacotes LaTeX necessários pela primeira vez.

**Solução:**
- **Isso é normal!** Aguarde pacientemente (2-5 minutos)
- MiKTeX baixa pacotes automaticamente conforme necessário
- Conversões seguintes serão rápidas (segundos)
- Não cancele o processo

**Dica:** Execute uma conversão de teste com arquivo pequeno primeiro:
```bash
echo "# Teste" > teste.md
python md_para_pdf.py teste.md
```

---

### Problema 4: Erro de encoding Unicode (PDF)

**Sintoma:**
```
UnicodeDecodeError: 'charmap' codec can't decode byte 0x8f
```

**Causa:** Saída do LaTeX contém caracteres especiais que Python não consegue decodificar.

**Solução:**
- **Já corrigido no script!** Versão atual usa `encoding='utf-8', errors='replace'`
- Se ainda ocorrer, atualize o script `md_para_pdf.py`
- O PDF é gerado corretamente mesmo com esse erro

**Verificar se PDF foi criado:**
```bash
dir README.pdf
```

---

### Problema 5: "Arquivo não encontrado"

**Sintoma:**
```
❌ Erro: Arquivo não encontrado: documento.md
```

**Causa:** Caminho do arquivo está incorreto.

**Solução:**

1. **Verificar se arquivo existe:**
```bash
dir documento.md
```

2. **Usar caminho correto:**
```bash
# Caminho relativo
python md_para_word.py documento.md

# Caminho absoluto
python md_para_word.py "C:\Users\...\documento.md"

# Caminho com espaços (usar aspas)
python md_para_word.py "Meu Documento.md"
```

3. **Navegar para pasta correta:**
```bash
cd pasta-do-documento
python ../ferramentas/md_para_word.py documento.md
```

---

### Problema 6: Marca d'água não aparece no PDF

**Sintoma:**
PDF gerado, mas sem marca d'água visível.

**Causa:** Pacote LaTeX `draftwatermark` não instalado.

**Solução:**
- MiKTeX baixa automaticamente na primeira vez
- Se não funcionar, instalar manualmente:

```bash
# Abrir MiKTeX Console
miktex-console

# Ir em "Packages" → Buscar "draftwatermark" → Install
```

---

### Problema 7: Conversão funciona mas arquivo não abre

**Sintoma:**
Conversão reporta sucesso, mas Word/PDF não abre.

**Causa:** Arquivo corrompido ou incompleto.

**Solução:**

1. **Verificar tamanho do arquivo:**
```bash
dir README.docx
dir README.pdf
```

Se tamanho for 0 KB ou muito pequeno, houve erro.

2. **Verificar logs:**
```bash
type ..\logs\2026-01-24-conversoes.log
```

3. **Tentar com arquivo simples:**
```bash
echo "# Teste\n\nConteúdo de teste." > teste.md
python md_para_word.py teste.md
```

---

### Problema 8: Script Python não executa

**Sintoma:**
```
'python' não é reconhecido como um comando interno ou externo
```

**Causa:** Python não está instalado ou não está no PATH.

**Solução:**

1. **Instalar Python:**
```bash
winget install Python.Python.3.12
```

2. **Verificar instalação:**
```bash
python --version
```

3. **Se instalado mas não funciona, usar caminho completo:**
```bash
C:\Users\[usuario]\AppData\Local\Programs\Python\Python39\python.exe md_para_word.py documento.md
```

---

### Problema 9: Permissão negada ao salvar arquivo

**Sintoma:**
```
PermissionError: [Errno 13] Permission denied: 'documento.docx'
```

**Causa:** Arquivo está aberto em outro programa (Word, Adobe Reader).

**Solução:**
1. Fechar o arquivo em todos os programas
2. Tentar novamente
3. Se persistir, salvar com nome diferente:

```bash
python md_para_word.py documento.md --output documento-novo.docx
```

---

### Problema 10: Conversão em lote não funciona

**Sintoma:**
Tentando converter múltiplos arquivos, mas só o primeiro funciona.

**Solução:**

**Windows CMD:**
```cmd
for %f in (*.md) do python md_para_word.py %f
```

**PowerShell:**
```powershell
Get-ChildItem *.md | ForEach-Object { python md_para_word.py $_.Name }
```

---

## 🔧 Configuração Completa do Ambiente (Passo a Passo)

Para evitar todos os problemas acima, siga esta configuração completa:

### 1. Instalar Dependências
```bash
# Python
winget install Python.Python.3.12

# Pandoc
winget install --id JohnMacFarlane.Pandoc

# MiKTeX (para PDFs)
winget install MiKTeX.MiKTeX
```

### 2. Adicionar ao PATH (PowerShell como Administrador)
```powershell
# Adicionar Pandoc
$env:PATH += ";$env:LOCALAPPDATA\Pandoc"

# Adicionar MiKTeX
$env:PATH += ";C:\Program Files\MiKTeX\miktex\bin\x64"

# Tornar permanente (opcional)
[Environment]::SetEnvironmentVariable("Path", $env:PATH, [System.EnvironmentVariableTarget]::User)
```

### 3. Verificar Instalação
```bash
python --version
pandoc --version
xelatex --version
```

### 4. Teste Rápido
```bash
# Criar arquivo de teste
echo "# Teste\n\nEste é um teste." > teste.md

# Testar Word
python md_para_word.py teste.md

# Testar PDF (pode demorar na primeira vez)
python md_para_pdf.py teste.md

# Verificar arquivos gerados
dir teste.docx
dir teste.pdf
```

Se todos os comandos funcionarem, está tudo pronto! ✅

---

## 📞 Ainda com Problemas?

Se nenhuma solução acima funcionou:

1. **Verificar versões:**
```bash
python --version  # Deve ser 3.8+
pandoc --version  # Deve ser 2.0+
xelatex --version # Deve mostrar MiKTeX
```

2. **Verificar logs de erro:**
```bash
type ..\logs\2026-01-24-conversoes.log
```

3. **Executar com debug:**
```bash
python -v md_para_word.py documento.md
```

4. **Contatar suporte:**
- Email: [seu-email]
- Canal de comunicação: [seu-canal]

---

## 📚 Exemplos Completos

### Exemplo 1: Contrato Jurídico
```bash
# Gerar contrato em Markdown (via Kiro)
# Arquivo: contrato-cliente-x.md

# Converter para Word com template jurídico
python md_para_word.py contrato-cliente-x.md --template juridico

# Converter para PDF assinável
python md_para_pdf.py contrato-cliente-x.md --assinavel

# Resultado:
# - contrato-cliente-x.md (original)
# - contrato-cliente-x.docx (para revisão)
# - contrato-cliente-x.pdf (para assinatura)
```

### Exemplo 2: Relatório de Compliance
```bash
# Gerar relatório em Markdown (via Kiro)
# Arquivo: relatorio-auditoria-q1.md

# Converter para Word com template compliance
python md_para_word.py relatorio-auditoria-q1.md --template compliance

# Converter para PDF com marca d'água
python md_para_pdf.py relatorio-auditoria-q1.md --marca-dagua "CONFIDENCIAL"

# Resultado:
# - relatorio-auditoria-q1.md (original)
# - relatorio-auditoria-q1.docx (para revisão)
# - relatorio-auditoria-q1.pdf (com marca d'água)
```

### Exemplo 3: Política de RH
```bash
# Gerar política em Markdown (via Kiro)
# Arquivo: politica-home-office.md

# Converter para Word com template RH
python md_para_word.py politica-home-office.md --template rh

# Converter para PDF padrão
python md_para_pdf.py politica-home-office.md

# Resultado:
# - politica-home-office.md (original)
# - politica-home-office.docx (para aprovação)
# - politica-home-office.pdf (para distribuição)
```

---

## 🔗 Referências

- [Documentação do Pandoc](https://pandoc.org/MANUAL.html)
- [Análise de Segurança do Pandoc](../../Tecnologias/kiro.md)
- [CVE-2025-51591](https://www.opencve.io/cve/CVE-2025-51591)
- [MiKTeX Documentation](https://miktex.org/docs)

---

**Última atualização:** 2026-01-24  
**Versão:** 1.0  
**Autor:** Projeto Kiro para Não-Dev
