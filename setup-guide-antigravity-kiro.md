# Guia de Configuração: Google Antigravity vs AWS Kiro

Este guia compara as duas principais IDEs com IA (Antigravity e Kiro) e mostra como configurar regras, automações e integrações em cada uma.

---

## 📑 Índice

- [Tabela Mestra: Antigravity vs. Kiro](#tabela-mestra-antigravity-vs-kiro)
- [Guia de Configuração Técnica](#guia-de-configuração-técnica)
  - [1. Configurando no Google Antigravity](#1-configurando-no-google-antigravity)
  - [2. Configurando no AWS Kiro](#2-configurando-no-aws-kiro)
- [Diferenças Críticas para Lembrar](#diferenças-críticas-para-lembrar)
- [Tabela de Convenções de Arquivos](#tabela-de-convenções-de-arquivos-antigravity-vs-kiro)
- [Nuances Importantes de Nomenclatura](#nuances-importantes-de-nomenclatura)
  - [1. Antigravity: O Nome do Arquivo é o Gatilho](#1-google-antigravity-o-nome-do-arquivo-é-o-gatilho)
  - [2. Kiro: O Poder do Frontmatter](#2-aws-kiro-o-poder-do-frontmatter-metadados)
  - [3. Arquivos Obrigatórios](#3-arquivos-obrigatórios-não-renomeie)

---

### Tabela Mestra: Antigravity vs. Kiro

| Conceito / Função | Definição | **Google Antigravity** (Implementação) | **AWS Kiro** (Implementação) |
| :--- | :--- | :--- | :--- |
| **Filosofia Central** | Como a IA aborda o desenvolvimento. | **Agent-First / Assíncrono:** Agentes paralelos gerenciados via "Mission Control". Foco em *Artifacts* visuais. | **Spec-Driven (SDD):** Fluxo sequencial obrigatório: Requisitos → Design → Código. Foco em estrutura. |
| **Regras Globais** | Diretrizes que se aplicam a *todos* os projetos do usuário. | **Arquivo `GEMINI.md`**<br>📍 `~/.gemini/GEMINI.md`<br>📝 Texto livre (Markdown). | **Global Steering**<br>📍 `~/.kiro/steering/*.md`<br>📝 Markdown com Frontmatter YAML. |
| **Regras de Workspace** | Diretrizes específicas para o projeto atual (stack, linter). | **Rules** (ou `.cursorrules`)<br>📍 `.agent/rules/*.md`<br>📍 `.cursorrules` (raiz - legado/compatibilidade). | **Workspace Steering**<br>📍 `.kiro/steering/*.md`<br>📍 `AGENTS.md` (raiz). |
| **Controle de Contexto** | Como regras são ativadas para não lotar a memória da IA. | **Divulgação Progressiva (Skills):** O agente decide ler a regra/skill baseada na descrição semântica. | **Inclusão Condicional:** Metadados YAML definem gatilhos (ex: `inclusion: fileMatch` para arquivos .ts ou `manual` via chat). |
| **Habilidades Extras** | Pacotes de ferramentas/scripts sob demanda. | **Skills**<br>📍 `.agent/skills/<nome>/`<br>📂 Contém `SKILL.md` + scripts + recursos. | **Powers**<br>📦 Pacote tudo-em-um (MCP + Regras + Hooks).<br>⚡ Ativado por palavras-chave no chat. |
| **Automação** | Ações programadas ou atalhos. | **Workflows**<br>📍 `.agent/workflows/`<br>⌨️ Acionado via comando `/` no chat (ex: `/test`). | **Hooks**<br>📍 `.kiro/hooks/`<br>⚡ Acionado por eventos (ex: ao salvar arquivo, ao parar agente). |
| **Planejamento** | Como a IA estrutura o trabalho antes de codar. | **Implementation Plan & Task List**<br>📄 Artefatos gerados dinamicamente no chat/interface. | **Specs (Arquivos Físicos)**<br>📄 `requirements.md` (EARS)<br>📄 `design.md`<br>📄 `tasks.md`. |
| **Conexão Externa** | Acesso a bancos de dados e APIs locais. | **MCP (Nativo + Store)**<br>🔌 Configurado via UI "MCP Store" ou JSON. Inclui "Browser Subagent" nativo. | **MCP + Powers**<br>🔌 Configurado via `mcp.json` ou embutido em Powers. |

---

### Guia de Configuração Técnica

Para utilizar dado do NotebookLM ou criar regras personalizadas, use os modelos abaixo.

#### 1. Configurando no Google Antigravity

**Cenário de exemplo:** Você quer que o agente consulte conteúdo criado pelo NotebookLM.

*   **Onde salvar:** Crie o arquivo `.agent/rules/architecture.md`.
*   **Conteúdo do arquivo:**
    ```markdown
    # Regras de Arquitetura (Fonte: NotebookLM)

    O agente deve estritamente seguir os padrões definidos abaixo ao gerar código:
    1. Nunca use 'try-except' genérico (bare except).
    2. Leia o arquivo 'docs/specs.md' antes de iniciar qualquer plano.
    ```
*   **Como ativar:** O Antigravity lê automaticamente os arquivos em `.agent/rules/` no início da sessão. Se quiser forçar, você pode criar um **Workflow** em `.agent/workflows/check-specs.md`:
    ```markdown
    ---
    description: Valida o código contra as specs do NotebookLM
    ---
    1. Leia o arquivo `docs/specs.md`.
    2. Analise o código atual.
    3. Liste violações da arquitetura.
    ```
    *Uso:* Digite `/check-specs` no chat.

#### 2. Configurando no AWS Kiro

**Cenário de exemplo:** Você quer que as regras de teste do NotebookLM apareçam apenas quando você estiver editando arquivos de teste.

*   **Onde salvar:** Crie o arquivo `.kiro/steering/testing.md`.
*   **Conteúdo do arquivo (Note o Frontmatter YAML):**
    ```markdown
    ---
    inclusion: fileMatch
    fileMatchPattern: "**/*.test.ts"
    ---
    # Padrões de Teste (Fonte: NotebookLM)

    1. Cada teste deve ter um 'describe' block claro.
    2. Mockar todas as chamadas externas AWS.
    ```
*   **Como ativar:** O Kiro ativará essas regras *automaticamente* e *apenas* quando você abrir ou criar um arquivo que termine em `.test.ts`. Isso economiza tokens e mantém o contexto limpo.

**Cenário de exemplo:** Você quer injetar um manual completo apenas quando pedir.

*   **Onde salvar:** `.kiro/steering/manual-completo.md`.
*   **Conteúdo:**
    ```markdown
    ---
    inclusion: manual
    ---
    # Manual Completo do Sistema
    [... conteúdo gigante do NotebookLM ...]
    ```
*   **Como ativar:** Digite `#manual-completo` no chat para puxar esse contexto específico.

### Diferenças Críticas para Lembrar

1.  **Compatibilidade do Cursor:** O **Antigravity** lê o arquivo `.cursorrules` para facilitar a migração, mas o **Kiro** não (ele usa seu próprio sistema ou `AGENTS.md`).
2.  **O "Cérebro" do Projeto:**
    *   No **Kiro**, o "cérebro" são os arquivos **Specs** (`requirements.md`, etc) que você *deve* editar e aprovar. É a fonte da verdade.
    *   No **Antigravity**, o "cérebro" é o **Contexto da Sessão** e os **Artifacts** (Planos). Para persistência de longo prazo entre sessões (evitar amnésia), a comunidade recomenda criar um arquivo `project_brain.json` ou similar na raiz e criar uma regra para o agente sempre lê-lo.

---

### Tabela de Convenções de Arquivos: Antigravity vs. Kiro

| Tipo de Arquivo | Google Antigravity (Convenção/Caminho) | AWS Kiro (Convenção/Caminho) | Regra de Nomenclatura |
| :--- | :--- | :--- | :--- |
| **Configuração Global** | `~/.gemini/GEMINI.md` | `~/.kiro/steering/*.md` | **AG:** Nome **fixo e obrigatório**. O sistema busca exatamente `GEMINI.md`.<br>**Kiro:** Flexível. Pode ter vários arquivos (ex: `global-security.md`). |
| **Regras de Projeto** | `.agent/rules/*.md`<br>*(Legado: `.cursorrules` na raiz)* | `.kiro/steering/*.md` | **AG:** Flexível. O agente lê todos os `.md` nesta pasta.<br>**Kiro:** Flexível. O comportamento é definido pelo cabeçalho YAML dentro do arquivo (Frontmatter). |
| **Contexto Mestre** | Não possui um arquivo mestre fixo na raiz (usa `.agent/rules/`). | `AGENTS.md` (na raiz) | **Kiro:** Nome **fixo**. Se existir na raiz, é sempre lido como instrução base ("Always Included"). |
| **Automação (Scripts)** | `.agent/workflows/<nome>.md` | `.kiro/hooks/*.kiro.hook` | **AG:** O nome do arquivo define o comando (ex: `test.md` vira `/test`).<br>**Kiro:** Arquivo JSON. O gatilho é definido internamente (ex: `on: fileSave`). |
| **Habilidades (Skills)** | `.agent/skills/<pasta>/SKILL.md` | Pacotes "Powers" (via UI ou repo) contendo `POWER.md` | **AG:** A pasta define o nome da skill, mas o arquivo de definição **deve** ser `SKILL.md`.<br>**Kiro:** Usa `POWER.md` para definições. |
| **Planejamento (Specs)** | *Gerado na UI (Task List/Plan)* | `.kiro/specs/<feature>/` contendo:<br>`requirements.md`<br>`design.md`<br>`tasks.md` | **Kiro:** Nomes **fixos** para o fluxo de especificação funcionar (Requisitos → Design → Tarefas). |
| **Conexão Externa** | Configurado via UI (MCP Store) | `.vscode/mcp.json` ou `.cursor/mcp.json` | **Kiro:** Segue o padrão de configuração JSON compatível com VS Code/Cursor. |

---

### Nuances Importantes de Nomenclatura

#### 1. Google Antigravity: O Nome do Arquivo é o Gatilho
No Antigravity, a nomenclatura dos arquivos na pasta de **Workflows** (`.agent/workflows/`) é funcional, não apenas organizacional.
*   **Como funciona:** Se você criar um arquivo chamado `deploy-prod.md`, você ativará essa automação digitando `/deploy-prod` no chat.
*   **Regra:** Use hífens em vez de espaços e mantenha nomes curtos para facilitar a digitação do comando.

#### 2. AWS Kiro: O Poder do "Frontmatter" (Metadados)
Diferente do Antigravity, onde colocar um arquivo na pasta de regras significa que ele será lido, o Kiro usa metadados no topo do arquivo (Frontmatter YAML) para decidir **quando** ler o arquivo. O nome do arquivo importa menos do que o conteúdo do cabeçalho.

*   **Exemplo de Arquivo Kiro (`.kiro/steering/react-rules.md`):**
    ```yaml
    ---
    inclusion: fileMatch
    fileMatchPattern: "**/*.tsx"
    ---
    # Regras para React...
    ```
    *Isso significa: "Só leia este arquivo se o usuário estiver editando um arquivo .tsx".*

#### 3. Arquivos Obrigatórios (Não Renomeie)
*   **`GEMINI.md` (Antigravity):** É a "constituição" do seu agente. Se você renomear para `regras.md` na pasta `~/.gemini/`, ele será ignorado.
*   **`SKILL.md` (Antigravity):** Dentro de uma pasta de habilidade (ex: `.agent/skills/revisao-codigo/`), o arquivo de instrução precisa ser `SKILL.md`. Se você chamá-lo de `instrucoes.md`, a skill não carregará.
*   **`requirements.md`, `design.md`, `tasks.md` (Kiro):** O sistema de "Spec-Driven Development" do Kiro procura especificamente por essa tríade de arquivos para gerenciar o estado do projeto e o progresso das tarefas.

# Como funcionaria para nossas ferramentas?

* **Antigravity:** Focaremos em encapsular isso como uma **Skill** (Habilidade) que o agente sabe que possui e como diagnosticar erros.
* **Kiro:** Focaremos em **Steering** (Diretrizes) para que ele saiba *quando* oferecer a conversão e **Hooks** para automação.

Aqui está a configuração passo a passo para cada um.

---

### 1. Configuração no Google Antigravity

No Antigravity, trataremos isso como um pacote de habilidades. O agente precisa saber: "Eu tenho ferramentas de conversão instaladas em tal pasta e sei como resolver erros comuns."

#### 📂 Estrutura de Pastas

```text
.agent/
├── skills/
│   └── document-converter/
│       ├── scripts/          <-- Coloque os .py aqui
│       ├── logs/             <-- O script salvará aqui
│       └── SKILL.md          <-- O cérebro da operação
├── workflows/
│   ├── to-pdf.md             <-- Atalho rápido
│   └── to-word.md            <-- Atalho rápido

```

#### 📄 Arquivo: `.agent/skills/document-converter/SKILL.md`

Este arquivo ensina o agente a usar a ferramenta e, crucialmente, a resolver os problemas listados no README.

```markdown
# Skill: Conversor Corporativo (Word/PDF)

## Capacidades
Você possui scripts Python locais para converter Markdown em formatos corporativos seguros.
Localização dos scripts: `.agent/skills/document-converter/scripts/`

## Comandos
1. **Para Word:** `python md_para_word.py <arquivo> --template <juridico|rh|compliance>`
2. **Para PDF:** `python md_para_pdf.py <arquivo>`

## Protocolo de Segurança
- Os scripts removem automaticamente iframes e scripts. Se o usuário reclamar de conteúdo sumindo, explique que foi a sanitização de segurança (CVE-2025-51591).

## Auto-Diagnóstico (Troubleshooting)
Se ocorrer erro ao executar, verifique:
1. **"Pandoc not found":** O usuário precisa instalar via `winget install --id JohnMacFarlane.Pandoc`.
2. **"xelatex not found":** Necessário MiKTeX (`winget install MiKTeX.MiKTeX`).
3. **Lentidão no PDF:** A primeira execução baixa pacotes LaTeX. Diga ao usuário para aguardar.
4. **Erro de Permissão:** Peça para fechar o arquivo Word/PDF se estiver aberto.

```

#### 📄 Arquivo: `.agent/workflows/to-pdf.md`

Cria um comando `/to-pdf` no chat.

```markdown
---
description: Converte o arquivo Markdown atual ou especificado para PDF profissional.
---

1. Identifique o arquivo Markdown no contexto atual.
2. Execute o script: `python .agent/skills/document-converter/scripts/md_para_pdf.py <arquivo>`
3. Se falhar, consulte a seção "Troubleshooting" em `SKILL.md` e sugira a correção.
4. Confirme o caminho do arquivo gerado.

```

---

### 2. Configuração no AWS Kiro

No Kiro, a abordagem é orientada a especificações. Vamos configurar para que o Kiro sugira a conversão sempre que um arquivo de documentação for finalizado.

#### 📂 Estrutura de Pastas

```text
.kiro/
├── steering/
│   └── doc-production.md    <-- Regra contextual
├── hooks/
│   └── auto-convert.json    <-- Automação (Opcional)
tools/                       <-- Scripts na raiz ou pasta tools
    ├── md_para_word.py
    └── md_para_pdf.py

```

#### 📄 Arquivo: `.kiro/steering/doc-production.md`

Usa *Frontmatter* para ativar as regras apenas em arquivos relevantes.

```markdown
---
inclusion: fileMatch
fileMatchPattern: "**/*.md"
---

# Diretrizes de Produção de Documentos

## Ferramentas Disponíveis
Para este projeto, utilize os scripts em `/tools/` para gerar entregáveis.

### Quando usar:
- Se o arquivo for um contrato -> Use `md_para_word.py` com `--template juridico`.
- Se o arquivo for final -> Use `md_para_pdf.py`.

### Troubleshooting Conhecido
- **Erro Unicode:** O script já trata UTF-8, mas verifique se o arquivo de entrada não está corrompido.

### Comando de Exemplo
```bash
python tools/md_para_pdf.py ${currentFile} --output saida/${currentFileBase}.pdf

```

```

#### 📄 Arquivo: `.kiro/hooks/auto-convert.json` (Automação Avançada)
Isso permite que o Kiro execute o script automaticamente ao salvar, se configurado no ambiente.

```json
{
  "hooks": [
    {
      "name": "Gerar PDF ao Salvar Contratos",
      "event": "onFileSave",
      "pattern": "contratos/*.md",
      "command": "python tools/md_para_pdf.py ${filePath}",
      "blocking": false
    }
  ]
}

```

---

### 🚧 Preparação do Ambiente (Crucial para ambos)

Como o README deixa claro que existem dependências de sistema (`winget`), o agente não conseguirá "auto-instalar" isso se estiver rodando em um container Linux padrão sem permissões.

**Ação Recomendada para o Usuário:**
Antes de deixar o agente rodar os comandos, você deve criar um arquivo de verificação inicial.

**Sugestão de Prompt Inicial para o Agente:**

> "Agente, leia o arquivo README.md. Verifique se meu ambiente tem Python, Pandoc e MiKTeX instalados rodando os comandos de versão (`--version`). Se faltar algo, me avise para eu instalar manualmente via winget antes de tentarmos converter."

### Resumo das Diferenças na Prática

| Característica | Google Antigravity | AWS Kiro |
| --- | --- | --- |
| **Ativação** | Via comando explícito (`/to-pdf`) ou Agente lendo a Skill. | Contextual (ao editar um `.md`) ou Automático (Hook ao salvar). |
| **Resolução de Erros** | O agente lê o `SKILL.md` e tenta "conversar" sobre o erro. | O agente segue as instruções do `steering` estritamente. |
| **Local dos Scripts** | Geralmente dentro da pasta da Skill para portabilidade. | Geralmente na pasta `tools` ou raiz do projeto. |