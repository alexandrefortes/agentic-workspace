---
inclusion: always
---

# Nomenclatura de Arquivos

O nome dos arquivos precisa ser o título da ideia em lowercase separado com hífen e sem caracteres latinos. Por ex: "ç" vira "c".

**Exemplos:**
- "Ideia de Automação.md" → `ideia-de-automacao.md`

---

# Conversão de Documentos (Markdown → Word/PDF)

Quando o usuário pedir para gerar arquivos Word (.docx) ou PDF (.pdf), você DEVE usar os scripts de conversão disponíveis neste projeto.

## Scripts Disponíveis

**Localização:** `ferramentas/`

1. **md_para_word.py** - Converte Markdown para Word
2. **md_para_pdf.py** - Converte Markdown para PDF

## Como Usar

### Conversão Básica para Word
```bash
python ferramentas/md_para_word.py arquivo.md
```

### Conversão Básica para PDF
```bash
python ferramentas/md_para_pdf.py arquivo.md
```

### Com Templates (Word)
```bash
python ferramentas/md_para_word.py arquivo.md --template juridico
python ferramentas/md_para_word.py arquivo.md --template rh
python ferramentas/md_para_word.py arquivo.md --template compliance
python ferramentas/md_para_word.py arquivo.md --template comercial
```

### PDF com Recursos Especiais
```bash
# PDF assinável
python ferramentas/md_para_pdf.py arquivo.md --assinavel

# PDF com marca d'água
python ferramentas/md_para_pdf.py arquivo.md --marca-dagua "CONFIDENCIAL"
```

### Especificar Arquivo de Saída
```bash
python ferramentas/md_para_word.py arquivo.md --output saida/documento.docx
python ferramentas/md_para_pdf.py arquivo.md --output saida/documento.pdf
```

### Regras Importantes

1. **SEMPRE use os scripts do projeto** - Não sugira ferramentas externas ou métodos alternativos
2. **Verifique se o arquivo Markdown existe** antes de tentar converter
3. **Use caminhos relativos** ao executar os scripts
4. **Informe o usuário sobre o sucesso** da conversão e o tamanho do arquivo gerado
5. **Se houver erro**, consulte a documentação em `ferramentas/README.md#-troubleshooting`

**Exemplo de resposta:**
```
✅ Documento criado com sucesso!

Arquivos gerados:
- proposta-comercial.md (original)
- proposta-comercial.docx (15.2 KB)
- proposta-comercial.pdf (45.8 KB)
```

---

## Segurança

Os scripts têm sanitização automática para remover tags perigosas:
- `<iframe>` - Previne SSRF
- `<script>` - Previne execução de código
- `<object>` e `<embed>` - Previne injeção

Todas as conversões são registradas em logs de auditoria em `logs/`.

---

## Quando NÃO Usar os Scripts

- Quando o usuário pedir apenas o Markdown (não converter automaticamente)