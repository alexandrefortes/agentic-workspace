[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)

# Agentic Workspace 

> Produtividade com IA Contextual para Profissionais Não-Técnicos

![Agentic IDE for Non-Devs Cover](cover2.png)

> 💡 **Dica para Iniciantes:**  
> Não sabe como configurar o ambiente? **Peça ao próprio Kiro/Antigravity!**  
> 
> Basta dizer:  
> *"Configure o ambiente de conversão de documentos para mim*
> - Ler os [requisitos em `ferramentas/conversao-word-e-pdf/requirements.txt`](ferramentas/conversao-word-e-pdf/requirements.txt)
> - Ler a [documentação de troubleshooting em `ferramentas/conversao-word-e-pdf/README.md#-troubleshooting`](ferramentas/conversao-word-e-pdf/README.md#-troubleshooting)
> - Checar se Pandoc e MiKTeX estão instalados, se não, instalar
> - Configurar o PATH do sistema
> - Testar as conversões e tentar corrigir até conseguir
> - Reportar se tudo funcionou" no RELATORIO-CONFIGURACAO.md

---

## 🆚 Antigravity vs Kiro: Qual Escolher?

Antes de decidir qual ferramenta usar, veja a comparação entre as duas principais opções recomendadas:

| Produto | Plano | Preço/mês | O que vem no plano (relevante p/ uso pessoal) | Modelos (o que dá para escolher/usar) | Como o limite é medido |
|---------|-------|-----------|-----------------------------------------------|---------------------------------------|------------------------|
| **Amazon Kiro** | **Pro** | **US$ 20** ([Kiro][1]) | IDE/ambiente agentic; inclui **1.000 créditos/mês** e **overage pay-per-use** a **US$ 0,04/crédito** ([Kiro][1]) | Apenas modelos da Anthropic **Sonnet 4.5 / Haiku 4.5 / Opus 4.5** ([Kiro][1]) | **Créditos** (unidade de trabalho por tarefa; custos variam por modelo) ([Kiro][1]) |
| **Google Antigravity** | **Google AI Pro** | **R$ 96,99** ([Gemini][2]) | Pacote Google AI com **2 TB**, **NotebookLM com benefícios**, **Gemini Pro** ([Google One][3]) | Antigravity tem **Gemini 3 Pro** e **Claude 4.5 Opus**([Google Help][4]) | Limites mais altos no Antigravity com **atualização a cada 5 horas** |

[1]: https://kiro.ai/pricing
[2]: https://one.google.com/about/plans
[3]: https://one.google.com/about/ai-premium
[4]: https://support.google.com/gemini/answer/15785754

---

## 📋 Resumo 

Usar o Amazon Kiro ou Google Antigravity como ferramenta de produtividade para profissionais não-técnicos (Ex.: Jurídico, RH, Compliance, Comercial) criarem documentos, relatórios e análises de forma assistida por IA, substituindo Custom GPTs com uma solução mais poderosa e contextualizada.

---

## 🎯 Problema

Colaboradores de áreas não-técnicas gastam tempo significativo em tarefas repetitivas de criação de documentos:
- **Jurídico:** Contratos, pareceres, análises de documentos
- **RH:** Políticas, comunicados, descrições de cargo
- **Compliance:** Relatórios de auditoria, análises de risco
- **Comercial:** Propostas comerciais, apresentações, relatórios de vendas

Atualmente, muitos usam Custom GPTs do ChatGPT, mas essa solução tem limitações:
- Não acessa arquivos locais do PC
- Controle de contexto limitado (com múltiplos documentos não fica claro como a IA escolhe quais documentos estão sendo usados)
- Sem integração com processos internos
- Sem controle de versão ou rastreabilidade

---

## 💡 Solução Proposta

Usar o **Amazon Kiro** ou **Google Antigravity** como assistentes de produtividade para quaquer atividade, não apenas desenvolvimento de software, aproveitando suas capacidades avançadas:

- **Contexto Dinâmico (Steering Files ou skills):** Definir regras de negócio, tom de voz e formatos específicos por projeto (ex: "sempre use linguagem formal em contratos").
- **Conexão com Dados Reais:** Conectar o agente a bancos de dados, APIs (ex: NotebookLM, Notion, Google Sheets, emails).
- **Planejamento Estruturado:** O agente cria planos de implementação (Antigravity) ou segue especificações rígidas (Kiro) para garantir qualidade antes de executar.
- **Leitura Inteligente de Múltiplos Arquivos:** O agente consegue analisar pastas inteiras com PDFs, planilhas, imagens e documentos simultaneamente.
- **Criação de Código/Ferramentas Sob Demanda:** Descrever o problema em linguagem natural e o agente gera código/ferramentas para uso pontual ou recorrente (ex: cruzar planilhas, renomear arquivos em lote, extrair dados de PDFs). Se você já tem ferramentas locais do seu PC (como os scripts de conversão deste projeto), o agente aprende a usar.

### Exemplos de Como Funciona

```
📁 Pasta de Entrada (Insumos)
   ├── contratos-referencia/
   ├── templates/
   ├── documentos-base.pdf
   └── diretrizes.md

         ↓ (Kiro processa)

🤖 Amazon Kiro + Steering Files ou Google Antigravity + Skills
   ├── Lê todos os arquivos (PDF, Word, Excel, imagens)
   ├── Aplica diretrizes de contexto dinâmicas
   ├── Gera documentos seguindo padrões da empresa
   └── Mantém rastreabilidade e versionamento

         ↓ (Saída)

📁 Pasta de Saída (Entregáveis)
   ├── contrato-cliente-x-v1.docx
   ├── parecer-juridico-caso-y.pdf
   └── relatorio-analise-z.md
```

### Vantagens sobre Custom GPTs

| Aspecto | Custom GPT | IDE Agentica |
|---------|-----------|-------------|
| **Acesso a arquivos locais** | ❌ Limitado (precisa copiar/colar) | ✅ Sim (lê pastas inteiras) |
| **Contexto dinâmico** | ❌ Fixo por GPT / Pouco controle | ✅ Steering Files por projeto |
| **Integração com processos** | ❌ Limitado | ✅ Sim (pode executar scripts, validações) |
| **Rastreabilidade** | ❌ Não | ✅ Git, versionamento automático |
| **Custo** | 💰 $20/usuário/mês | 💰 Licença única + VM |

---

## 🔧 Exemplos de Casos de Uso Práticos

### 1. Time Jurídico: Criação de Contratos

**Entrada:**
- Pasta com 10 contratos de referência (PDF)
- Template base (Word)
- Steering file com cláusulas obrigatórias e linguagem jurídica padrão
- Briefing do novo contrato (texto simples)

**Comando ao Kiro:**
> "Crie um contrato de prestação de serviços para o Cliente X, seguindo o template base e incluindo as cláusulas de proteção de dados conforme os contratos de referência. Prazo: 12 meses, valor: R$ 500k."

**Saída:**
- `contrato-cliente-x-v1.docx` (pronto para revisão)
- Checklist de conformidade automático
- Comparativo com contratos similares

---

### 2. Time de Compliance: Análise de Documentos

**Entrada:**
- 50 PDFs de notas fiscais
- Planilha de fornecedores homologados
- Steering file com regras de compliance
- Política de alçadas (PDF)

**Comando ao Kiro:**
> "Analise todas as notas fiscais e identifique: 1) Fornecedores não homologados, 2) Valores acima da alçada, 3) Inconsistências de data/valor. Gere relatório em Excel."

**Saída:**
- `relatorio-compliance-nf-2026-01.xlsx`
- Lista de exceções com justificativas
- Recomendações de ação

---

### 3. Time de RH: Criação de Políticas

**Entrada:**
- Políticas antigas (Word)
- Legislação trabalhista atualizada (PDF)
- Steering file com tom de voz da empresa
- Benchmark de mercado (Excel)

**Comando ao Kiro:**
> "Atualize a política de home office considerando a nova legislação e as práticas de mercado. Mantenha o tom acolhedor da empresa."

**Saída:**
- `politica-home-office-2026.docx`
- Comparativo com versão anterior (track changes)
- FAQ para colaboradores

---

### 4. Time Comercial: Propostas Personalizadas

**Entrada:**
- Catálogo de produtos (PDF)
- Histórico de vendas do cliente (Excel)
- Template de proposta (PowerPoint)
- Steering file com linguagem comercial

**Comando ao Kiro:**
> "Crie uma proposta comercial para renovação do Cliente Y, destacando produtos que ele já usa e sugerindo 3 upsells baseados no histórico."

**Saída:**
- `proposta-cliente-y-renovacao-2026.pptx`
- Planilha de precificação
- Email de apresentação

---

## 🔧 Conversão de Documentos

Este projeto inclui scripts Python para converter documentos Markdown em formatos corporativos (Word e PDF) com segurança e qualidade profissional.

> ⚠️ **Importante:** Veja o [guia completo de troubleshooting](ferramentas/conversao-word-e-pdf/README.md#-troubleshooting) se encontrar problemas na instalação ou conversão.

### Scripts Disponíveis

**Localização:** `ferramentas/conversao-word-e-pdf/`

1. **md_para_word.py** - Converte Markdown para Word (.docx)
2. **md_para_pdf.py** - Converte Markdown para PDF (.pdf)

Ambos os scripts implementam **sanitização automática** para mitigar vulnerabilidades do Pandoc (CVE-2025-51591 e CVE-2023-35936).

---

### Pré-requisitos

Antes de usar os scripts de conversão, certifique-se de ter instalado:

1. **Python 3.8+**
   ```bash
   winget install Python.Python.3.12
   python --version
   ```

2. **Pandoc** (para conversões)
   ```bash
   winget install --id JohnMacFarlane.Pandoc
   pandoc --version
   ```

3. **MiKTeX** (para PDFs de qualidade)
   ```bash
   winget install MiKTeX.MiKTeX
   xelatex --version
   ```

### Configuração do PATH

Se os comandos não funcionarem após instalação, adicione ao PATH permanentemente:

```powershell
# PowerShell
$env:PATH += ";$env:LOCALAPPDATA\Pandoc;C:\Program Files\MiKTeX\miktex\bin\x64"
```

Para configuração permanente, veja o [guia de troubleshooting](ferramentas/conversao-word-e-pdf/README.md#-troubleshooting).

---

### Como Usar

#### Conversão Básica

```bash
# Converter para Word
python ferramentas/conversao-word-e-pdf/md_para_word.py documento.md

# Converter para PDF
python ferramentas/conversao-word-e-pdf/md_para_pdf.py documento.md
```

#### Com Templates (Word)

```bash
python ferramentas/conversao-word-e-pdf/md_para_word.py documento.md --template juridico
python ferramentas/conversao-word-e-pdf/md_para_word.py documento.md --template rh
python ferramentas/conversao-word-e-pdf/md_para_word.py documento.md --template compliance
python ferramentas/conversao-word-e-pdf/md_para_word.py documento.md --template comercial
```

#### Especificar Arquivo de Saída

```bash
python ferramentas/conversao-word-e-pdf/md_para_word.py documento.md --output saida/documento.docx
python ferramentas/conversao-word-e-pdf/md_para_pdf.py documento.md --output saida/documento.pdf
```

---

### Segurança

Os scripts implementam sanitização automática para remover tags perigosas:
- `<iframe>` - Previne SSRF (CVE-2025-51591)
- `<script>` - Previne execução de código
- `<object>` e `<embed>` - Previne injeção

**Nível de risco:** BAIXO
- Processamos apenas documentos internos (Markdown gerado pelo Kiro)
- Ambiente isolado por design
- Sem processamento de HTML externo

Todas as conversões são registradas em logs de auditoria em `ferramentas/conversao-word-e-pdf/logs/`.

---

### Exemplos Práticos

#### Contrato Jurídico
```bash
python ferramentas/conversao-word-e-pdf/md_para_word.py contrato-cliente-x.md --template juridico
python ferramentas/conversao-word-e-pdf/md_para_pdf.py contrato-cliente-x.md
```

#### Política de RH
```bash
python ferramentas/conversao-word-e-pdf/md_para_word.py politica-home-office.md --template rh
python ferramentas/conversao-word-e-pdf/md_para_pdf.py politica-home-office.md
```

#### Relatório de Compliance
```bash
python ferramentas/conversao-word-e-pdf/md_para_word.py relatorio-auditoria.md --template compliance
python ferramentas/conversao-word-e-pdf/md_para_pdf.py relatorio-auditoria.md
```

#### Proposta Comercial
```bash
python ferramentas/conversao-word-e-pdf/md_para_word.py proposta-cliente-y.md --template comercial
python ferramentas/conversao-word-e-pdf/md_para_pdf.py proposta-cliente-y.md
```

---

### Troubleshooting

Se encontrar problemas, consulte:
- [Guia completo de troubleshooting](ferramentas/conversao-word-e-pdf/README.md#-troubleshooting)
- [Documentação dos scripts](ferramentas/conversao-word-e-pdf/README.md)

---

### Exemplo de Conversão

Este próprio README foi convertido usando os scripts do projeto:

📄 **Versões deste documento:**
- [Markdown](README.md) (você está aqui)
- [Word](README.docx) - ✅ Gerado com `md_para_word.py` (19.5 KB)
- [PDF](README.pdf) - ✅ Gerado com `md_para_pdf.py` (61.8 KB)

---

## 📁 Estrutura de Arquivos do Projeto

Veja a [documentação completa da estrutura](estrutura-projeto.md) para entender como organizar os arquivos.

---

## 🛡️ Segurança e Governança Recomendada se for usar em ambiente corporativo

### Ambiente Isolado Recomendado
- Kiro em **VM descartável** ou **Container Docker**
- Dados sensíveis **nunca** saem do ambiente corporativo

### Controles de Acesso
- Cada área tem sua própria VM/projeto
- Steering files específicos por área (Jurídico, RH, Compliance)
- Logs de auditoria de todos os comandos e arquivos gerados

### Aprovação e Revisão
- Documentos gerados são **rascunhos** (sempre precisam de revisão humana)
- Fluxo de aprovação mantido (Kiro acelera, não substitui aprovadores)
- Versionamento automático via Git

---

## 📊 Benefícios Esperados (WIP)

### Quantitativos (WIP)
- **Redução de ?%** no tempo de criação de documentos padrão
- **Aumento de ?%** na produtividade de tarefas repetitivas
- **ROI em ? meses** (considerando custo de licença + VM vs. horas economizadas)

### Qualitativos
- Maior consistência nos documentos (seguem sempre os padrões)
- Redução de erros (Kiro valida contra diretrizes)
- Pessoas focam em análise crítica, não em formatação
- Conhecimento institucional preservado (Steering files documentam padrões)

---

## 🚀 Plano de Implementação em Equipes (WIP)

### Fase 1: Piloto (2 meses)
- Escolher 1 área piloto
- Configurar VM isolada com Kiro
- Criar Steering files iniciais
- Treinar pessoas
- Medir resultados

### Fase 2: Expansão (3 meses)
- Expandir para 2-3 áreas adicionais
- Refinar Steering files com base no piloto
- Criar biblioteca de templates
- Documentar casos de uso

### Fase 3: Escala (6 meses)
- Disponibilizar para todas as áreas não-técnicas
- Criar programa de embaixadores
- Integrar com ferramentas corporativas (SharePoint, Jira)
- Medir ROI e ajustar

---

## 💰 Estimativa de Custos (WIP)

| Item | Custo Mensal |
|------|--------------|
| Licença Kiro Pro (uso pessoal) | US$ 20,00 |
| Licença Antigravity | ~R$ 100,00 |

**Economia esperada:** ? horas/mês × R$ ?/hora = R$ ?/mês = **R$ ?/ano**

**ROI:** ?% no primeiro ano

---

## ⚠️ Riscos e Mitigações

| Risco | Probabilidade | Impacto | Mitigação |
|-------|---------------|---------|-----------|
| Resistência cultural ("IA vai me substituir") | Alta | Alto | Comunicação clara: Kiro é assistente, não substituto. Foco em tarefas repetitivas. |
| Qualidade dos documentos gerados | Média | Alto | Sempre exigir revisão humana. Começar com casos simples. |
| Vazamento de dados sensíveis | Baixa | Crítico | Se ambiente corporativo, recomendo ambiente isolado e auditoria de logs. |
| Custo de manutenção maior que esperado | Média | Médio | Começar com piloto pequeno. Medir ROI e qualidade de treinamento antes de escalar. |
| Dependência de fornecedor (Amazon/Google) | Baixa | Médio | Avaliar alternativas (Cursor, Windsurf) no futuro. |

---

## 🔗 Referências

- [Análise de Segurança do Kiro](../../Tecnologias/kiro.md)
- [Comparativo de IDEs com IA](../../Tecnologias/comparativo-seguranca-ides-ia.md)
- [Scripts de Conversão](ferramentas/conversao-word-e-pdf/)
- [Steering Files de Exemplo](steering-files/)

---

## 👤 Sobre o Autor

**Alexandre Fortes**  
*Data & AI Executive @ Efí Bank*

Executivo de Dados e IA com atuação "hands-on". Especialista em colocar sistemas de LLM em produção (end-to-end), desde o desenho do problema até a entrega segura em operações críticas. 

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/alexandre-f-santana/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=for-the-badge&logo=github)](https://github.com/alexandrefortes)