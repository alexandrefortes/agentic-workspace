Aqui está o tutorial adaptado para o ecossistema do **AWS Kiro**.

Diferente do Antigravity, que foca em "Agentes" e "Workflows", o Kiro é estruturado em **Steering** (Direcionamento) e **Hooks** (Gatilhos de Eventos). Para implementar sua conversão de documentos de forma eficiente no Kiro, vamos quebrar seu arquivo monolítico original em componentes modulares que aproveitam a "Engenharia de Contexto Proativa" da ferramenta.

### Estrutura de Arquivos Sugerida

```text
.kiro/
├── steering/
│   ├── convencoes.md          # Regras sempre ativas (Nomenclatura)
│   └── manual-conversao.md    # Instruções das ferramentas (Sob demanda)
└── hooks/
    └── gerar-doc.kiro.hook    # O gatilho para automação (Comando /)
ferramentas/
└── conversao-word-e-pdf/      # Seus scripts Python (mantidos onde estão)
```

---

### Passo 1: Regras Globais (Sempre Ativas)
No Kiro, regras que devem ser seguidas o tempo todo usam o frontmatter `inclusion: always`. Isso garante que o agente nunca esqueça como nomear arquivos, sem que você precise pedir.

**Arquivo:** `.kiro/steering/convencoes.md`

```markdown
---
inclusion: always
---

# Convenções de Nomenclatura

O agente deve aplicar estritamente estas regras ao criar novos arquivos:

1.  **Formato:** Use `kebab-case` (lowercase com hífens).
2.  **Sanitização:** Remova acentos e caracteres não-ASCII (ex: "ç" -> "c", "ã" -> "a").
3.  **Exemplos:**
    - "Relatório Final.docx" -> `relatorio-final.docx`
    - "Ideia de Automação.md" -> `ideia-de-automacao.md`
```

---

### Passo 2: Manual de Ferramentas (Inclusão Manual)
Aqui está a grande mudança. Em vez de deixar as instruções dos scripts Python ocupando espaço na memória o tempo todo, configuramos como `inclusion: manual`. O Kiro só lerá este arquivo se você mencionar explicitamente `#manual-conversao` ou se um Hook o invocar.

**Arquivo:** `.kiro/steering/manual-conversao.md`

```markdown
---
inclusion: manual
---

# Manual de Conversão de Documentos

Você tem permissão para executar scripts Python locais para converter Markdown em DOCX/PDF.
**NUNCA** sugira ferramentas externas. Use APENAS os comandos abaixo.

## Scripts Disponíveis
Caminho base: `ferramentas/conversao-word-e-pdf/`

### Comandos de Execução
1. **Para Word (.docx):**
   `python ferramentas/conversao-word-e-pdf/md_para_word.py <input_file> [options]`
   *Templates:* `--template juridico`, `--template comercial`

2. **Para PDF (.pdf):**
   `python ferramentas/conversao-word-e-pdf/md_para_pdf.py <input_file> [--output <output_file>]`

## Protocolo de Execução
1. Verifique se o arquivo de entrada existe.
2. Execute o comando no terminal.
3. Valide se o arquivo de saída foi gerado.
4. Reporte o sucesso ao usuário com o caminho do arquivo gerado.
```

---

### Passo 3: Automação via Hook (Slash Command)
O Kiro não usa arquivos Markdown para automação ("Workflows") como o Antigravity; ele usa arquivos JSON chamados **Hooks**. Vamos criar um hook manual que adiciona um comando `/gerar-doc` ao seu chat. Quando acionado, ele injeta automaticamente as instruções do passo 2 e pede ao agente para rodar o script.

**Arquivo:** `.kiro/hooks/gerar-doc.kiro.hook`

```json
{
  "name": "Gerar Word/PDF",
  "description": "Converte o markdown atual para formatos finais usando scripts locais",
  "version": "1",
  "when": {
    "type": "manual"
  },
  "then": {
    "type": "askAgent",
    "prompt": "Por favor, converta o arquivo markdown principal deste contexto para PDF e Word.\n\n1. Leia as instruções em #[[file:.kiro/steering/manual-conversao.md]] para saber como usar os scripts.\n2. Gere uma versão PDF.\n3. Gere uma versão Word com template 'comercial'.\n4. Siga as convenções de nome em #[[file:.kiro/steering/convencoes.md]]."
  }
}
```

---

### Como usar no dia a dia

1.  **Vibe Coding:** Você está escrevendo código ou texto normalmente.
2.  **Ação:** Digite `/` no chat do Kiro.
3.  **Seleção:** Você verá "Gerar Word/PDF" na lista de comandos (graças ao hook manual).
4.  **Resultado:** O Kiro vai:
    *   Ler o arquivo de instruções (que estava "dormindo" até agora).
    *   Executar o script Python no terminal integrado.
    *   Entregar os arquivos finais seguindo sua regra de nomenclatura.

### Tabela de Adaptação: Antigravity vs. Kiro

| Recurso | Sua Implementação Antigravity | Implementação Kiro (Sugerida) | Vantagem Kiro |
| :--- | :--- | :--- | :--- |
| **Regras** | `.agent/rules/convencoes.md` | `.kiro/steering/convencoes.md` | Suporta metadados YAML nativos para controle fino. |
| **Ferramentas** | `.agent/skills/conversor/` | `.kiro/steering/manual-conversao.md` | Uso de `inclusion: manual` economiza tokens até ser invocado. |
| **Automação** | `.agent/workflows/gerar.md` | `.kiro/hooks/gerar-doc.kiro.hook` | O Hook JSON permite lógica programática (ex: disparar ao salvar arquivo). |
| **Gatilho** | Digitar `/gerar` | Digitar `/` e selecionar no menu | Integração visual na UI via menu de comandos. |