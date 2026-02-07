# 📁 Estrutura de Arquivos do Projeto

Este documento descreve a organização completa dos arquivos para implementação da solução Kiro para não-devs.

---

## 🗂️ Estrutura Completa

```
agentic-ide-for-non-devs/
├── README.md                          # Documento principal da ideia
├── estrutura-projeto.md               # Este arquivo
├── README.docx                        # Versão Word (gerada automaticamente)
├── README.pdf                         # Versão PDF (gerada automaticamente)
│
├── ferramentas/                       # Ferramentas de automação
│   ├── README.md                     # Índice de ferramentas disponíveis
│   └── conversao-word-e-pdf/         # Scripts de conversão
│       ├── md_para_word.py           # Converte Markdown → Word
│       ├── md_para_pdf.py            # Converte Markdown → PDF
│       ├── requirements.txt          # Dependências Python
│       ├── README.md                 # Documentação dos scripts
│       └── logs/                     # Logs de auditoria
│
├── steering-files/                    # Steering files por área
│   ├── juridico.md                   # Diretrizes para Jurídico
│   ├── rh.md                         # Diretrizes para RH
│   ├── compliance.md                 # Diretrizes para Compliance
│   ├── comercial.md                  # Diretrizes para Comercial
│   └── README.md                     # Documentação dos steering files
│
├── templates/                         # Templates corporativos
│   ├── contrato-base.docx            # Template de contrato
│   ├── relatorio-base.docx           # Template de relatório
│   ├── politica-base.docx            # Template de política
│   └── proposta-base.docx            # Template de proposta comercial
│
├── exemplos/                          # Exemplos de uso
│   ├── juridico/                     # Exemplo: criação de contrato
│   ├── rh/                           # Exemplo: criação de política
│   ├── compliance/                   # Exemplo: análise de documentos
│   └── comercial/                    # Exemplo: proposta comercial
│
└── docs/                              # Documentação adicional
    ├── instalacao.md                 # Guia de instalação
    ├── uso-basico.md                 # Guia de uso básico
    └── troubleshooting.md            # Solução de problemas
```

---

## 📂 Descrição dos Diretórios

### `/ferramentas`
Pasta principal para ferramentas de automação do projeto.

**Subpastas:**
- `conversao-word-e-pdf/`: Scripts Python para conversão automática de documentos

**Arquivos em `conversao-word-e-pdf/`:**
- `md_para_word.py`: Converte Markdown para Word com sanitização de segurança
- `md_para_pdf.py`: Converte Markdown para PDF com qualidade profissional
- `requirements.txt`: Lista de dependências Python necessárias
- `README.md`: Documentação completa dos scripts
- `logs/`: Logs de auditoria de conversões

**Uso típico:**
```bash
python ferramentas/conversao-word-e-pdf/md_para_word.py documento.md --template juridico
python ferramentas/conversao-word-e-pdf/md_para_pdf.py documento.md
```

---

### `/steering-files`
Arquivos de diretrizes que o Kiro lê automaticamente para cada área.

**Arquivos:**
- `juridico.md`: Linguagem formal, cláusulas obrigatórias, foro
- `rh.md`: Tom acolhedor, conformidade trabalhista
- `compliance.md`: Rigor técnico, rastreabilidade, auditoria
- `comercial.md`: Linguagem persuasiva, foco em valor

**Como funciona:**
- Kiro detecta a pasta do projeto (ex: `projetos/juridico/`)
- Carrega automaticamente o steering file correspondente
- Aplica as diretrizes na geração de documentos

---

### `/templates`
Templates corporativos em formato Word para aplicação automática.

**Arquivos:**
- `contrato-base.docx`: Cabeçalho, rodapé, numeração de cláusulas
- `relatorio-base.docx`: Logo, sumário executivo, estrutura padrão
- `politica-base.docx`: Formatação institucional, aprovações
- `proposta-base.docx`: Identidade visual, estrutura comercial

**Uso:**
Os scripts de conversão aplicam automaticamente o template correto baseado na área.

---

### `/exemplos`
Casos de uso completos com entrada, processamento e saída.

**Estrutura de cada exemplo:**
```
exemplos/juridico/
├── README.md                    # Descrição do caso de uso
├── entrada/                     # Arquivos de entrada
│   ├── contratos-referencia/
│   ├── template.docx
│   └── briefing.txt
├── saida/                       # Arquivos gerados
│   ├── contrato-cliente-x.md
│   ├── contrato-cliente-x.docx
│   └── contrato-cliente-x.pdf
└── comandos.txt                 # Comandos usados no Kiro
```

---

### `/docs`
Documentação adicional para instalação, uso e troubleshooting.

**Arquivos:**
- `instalacao.md`: Passo a passo para configurar o ambiente
- `uso-basico.md`: Tutorial para primeiros passos
- `troubleshooting.md`: Soluções para problemas comuns

---

## 🔄 Fluxo de Trabalho Típico

### 1. Usuário Inicia Projeto
```bash
# Criar pasta do projeto
mkdir projetos/juridico/contrato-cliente-x

# Adicionar arquivos de referência
cp contratos-antigos/* projetos/juridico/contrato-cliente-x/entrada/
```

### 2. Kiro Processa
```
# Kiro detecta pasta "juridico"
# Carrega steering-files/juridico.md automaticamente
# Lê todos os arquivos da pasta entrada/
# Gera documento.md seguindo diretrizes
```

### 3. Conversão Automática
```bash
# Kiro executa automaticamente:
python ferramentas/conversao-word-e-pdf/md_para_word.py documento.md --template juridico
python ferramentas/conversao-word-e-pdf/md_para_pdf.py documento.md

# Salva em:
projetos/juridico/contrato-cliente-x/saida/
```

### 4. Usuário Revisa
```
# Usuário abre documento.docx
# Faz revisões necessárias
# Aprova e envia
```

---

## 🎯 Convenções de Nomenclatura

### Arquivos Markdown
- Usar kebab-case: `contrato-cliente-x.md`
- Incluir data se necessário: `relatorio-2026-01-24.md`
- Versionar se necessário: `politica-home-office-v2.md`

### Pastas de Projeto
```
projetos/<area>/<tipo-documento>-<identificador>/
```

**Exemplos:**
- `projetos/juridico/contrato-cliente-abc/`
- `projetos/rh/politica-home-office/`
- `projetos/compliance/auditoria-q1-2026/`
- `projetos/comercial/proposta-cliente-xyz/`

### Arquivos de Saída
```
<nome-base>.<extensao>
```

**Exemplos:**
- `contrato-cliente-x.md` (original)
- `contrato-cliente-x.docx` (para revisão)
- `contrato-cliente-x.pdf`

---

## 🔐 Segurança e Organização

### Separação por Área
Cada área tem sua própria estrutura isolada:

```
projetos/
├── juridico/          # Apenas time Jurídico acessa
├── rh/               # Apenas time RH acessa
├── compliance/       # Apenas time Compliance acessa
└── comercial/        # Apenas time Comercial acessa
```

### Versionamento
Usar Git para rastrear mudanças:

```bash
# Commit após cada geração
git add projetos/juridico/contrato-cliente-x/
git commit -m "Gera contrato Cliente X - v1"

# Tag para versões importantes
git tag contrato-cliente-x-v1.0
```

### Logs de Auditoria
Scripts de conversão geram logs automaticamente:

```
ferramentas/conversao-word-e-pdf/logs/
├── 2026-01-24-conversoes.log
├── 2026-01-25-conversoes.log
└── ...
```

**Formato do log:**
```
2026-01-24 14:30:15 | usuario@empresa.com | md_para_word.py | contrato-cliente-x.md → contrato-cliente-x.docx | SUCESSO
```

---

## 📊 Métricas e Monitoramento

### Arquivos a Monitorar
- Número de conversões por dia/semana/mês
- Tempo médio de conversão
- Taxa de erro
- Distribuição por área (Jurídico, RH, Compliance, Comercial)

### Dashboard Sugerido
```
Conversões Hoje: 47
├── Jurídico: 18 (38%)
├── RH: 12 (26%)
├── Compliance: 10 (21%)
└── Comercial: 7 (15%)

Tempo Médio: 2.3s
Taxa de Sucesso: 98.5%
```

---

## 🚀 Próximos Passos

1. [ ] Criar estrutura de pastas completa
2. [ ] Implementar scripts de conversão
3. [ ] Criar steering files para cada área
4. [ ] Preparar templates corporativos
5. [ ] Documentar exemplos de uso
6. [ ] Testar fluxo completo
7. [ ] Treinar usuários piloto

---

**Última atualização:** 2026-01-24  
**Versão:** 1.0
