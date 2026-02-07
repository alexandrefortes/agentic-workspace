### 1. Regras de Projeto (`.agent/rules/`)
As regras de nomenclatura devem estar sempre ativas, pois afetam qualquer criação de arquivo.

*   **Local:** `.agent/rules/convencoes.md`
*   **Por que:** O Antigravity lê tudo nesta pasta automaticamente ao iniciar. Isso garante que o agente nunca "esqueça" como nomear arquivos.

```markdown
# Convenções de Nomenclatura de Arquivos

**Regra Crítica:** O agente DEVE seguir estritamente este padrão ao criar novos arquivos.

1.  **Formato:** `lowercase` com palavras separadas por hífen (`-`).
2.  **Caracteres:** Apenas ASCII. Remova acentos e caracteres especiais (ex: "ç" vira "c", "ã" vira "a").
3.  **Exemplos:**
    - "Ideia de Automação.md" → `ideia-de-automacao.md`
    - "Relatório Final.docx" → `relatorio-final.docx`
```

---

### 2. Habilidade (Skill) (`.agent/skills/`)
A lógica de conversão de documentos (Word/PDF) não precisa ocupar espaço na memória do agente o tempo todo. Ela deve ser uma **Skill** carregada apenas quando você pedir para converter algo. Isso evita o "tool bloat" (inchaço de ferramentas).

*   **Local:** Crie a pasta `.agent/skills/conversor-docs/` e dentro dela o arquivo `SKILL.md`.
*   **Por que:** O agente lerá a descrição e, se você pedir "Gere um PDF disso", ele carregará as instruções de como usar seus scripts Python.

**Conteúdo de `.agent/skills/conversor-docs/SKILL.md`:**

```markdown
---
name: conversor-docs
description: Converte arquivos Markdown para Word (.docx) ou PDF (.pdf) usando scripts Python locais. Use isso quando o usuário solicitar geração de documentos finais.
---

# Conversor de Documentos (Skill)

Você tem acesso a scripts Python robustos para conversão. **NUNCA** tente escrever seu próprio código de conversão ou sugerir ferramentas externas. Use APENAS os scripts abaixo.

## Ferramentas Disponíveis
Caminho base: `ferramentas/conversao-word-e-pdf/`

### 1. Gerar Word (.docx)
Comando:
`python ferramentas/conversao-word-e-pdf/md_para_word.py <arquivo_entrada> [opções]`

**Opções de Templates:**
- `--template juridico`
- `--template rh`
- `--template compliance`
- `--template comercial`

### 2. Gerar PDF (.pdf)
Comando:
`python ferramentas/conversao-word-e-pdf/md_para_pdf.py <arquivo_entrada> [--output <arquivo_saida>]`

## Fluxo de Trabalho Obrigatório
1. **Verifique** se o arquivo Markdown de entrada existe.
2. **Execute** o script usando o terminal integrado.
3. **Valide** se o arquivo de saída foi criado.
4. **Responda** ao usuário confirmando o nome e tamanho do arquivo gerado.

## Segurança e Auditoria
- Os scripts já possuem sanitização interna (removem iframes/scripts).
- Não é necessário validar injeção de código manualmente, confie no script.
```

---

### 3. Workflow (`.agent/workflows/`)
Para facilitar sua vida, você pode criar um "atalho" (slash command) para disparar essa ação sem precisar digitar muito.

*   **Local:** `.agent/workflows/gerar-doc.md`
*   **Uso:** Digite `/gerar-doc` no chat.

```markdown
---
description: Gera automaticamente os formatos Word e PDF do documento atual
---

1. Identifique o arquivo Markdown principal que estamos trabalhando.
2. Use a skill `conversor-docs` para gerar uma versão **PDF**.
3. Use a skill `conversor-docs` para gerar uma versão **Word** usando o template `comercial` (a menos que eu peça outro).
4. Liste os links para os arquivos gerados no chat.
```

### Resumo das Mudanças (Kiro → Antigravity)

| Recurso | No Kiro (Original) | No Antigravity (Sugerido) | Vantagem |
| :--- | :--- | :--- | :--- |
| **Nomenclatura** | `steering/global.md` | `.agent/rules/convencoes.md` | Sempre ativo, sem ocupar contexto com lógica de scripts. |
| **Scripts Python** | `inclusion: always` | `.agent/skills/conversor-docs/` | **Economia de Tokens.** O agente só lê o manual dos scripts quando necessário. |
| **Automação** | N/A | `.agent/workflows/gerar-doc.md` | Cria um comando `/gerar-doc` rápido e repetível. |

**Nota Importante sobre Global vs Workspace:**
Como seus scripts estão em uma pasta local do projeto (`ferramentas/...`), essas regras e skills devem ficar na pasta `.agent` do projeto (Workspace), e não na pasta global `~/.gemini/`. Se você colocar na global, o agente tentará rodar scripts que não existem em outros projetos.