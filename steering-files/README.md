# 🎯 Exemplos de Steering Files por Área

Arquivos de diretrizes que o Kiro lê automaticamente para aplicar padrões específicos.

---

## 📋 O que são Steering Files?

Steering files são arquivos Markdown que contêm instruções e diretrizes para o Kiro.

---

## 🗂️ Exemplos Disponíveis

### 1. `juridico.md`
**Quando é usado:** Projetos na pasta `projetos/juridico/**`

**Diretrizes:**
- Linguagem formal e técnica
- Cláusulas obrigatórias (LGPD, foro, rescisão)
- Numeração de cláusulas
- Conversão automática para Word + PDF

**Exemplo de uso:**
```
projetos/juridico/contrato-cliente-x/
└── Kiro carrega automaticamente juridico.md
```

---

### 2. `rh.md`
**Quando é usado:** Projetos na pasta `projetos/rh/**`

**Diretrizes:**
- Tom acolhedor e inclusivo
- Conformidade com legislação trabalhista
- Linguagem acessível
- Conversão automática para Word editável

**Exemplo de uso:**
```
projetos/rh/politica-home-office/
└── Kiro carrega automaticamente rh.md
```

---

### 3. `compliance.md`
**Quando é usado:** Projetos na pasta `projetos/compliance/**`

**Diretrizes:**
- Rigor técnico e objetividade
- Rastreabilidade de evidências
- Estrutura padronizada de relatórios
- Conversão automática para PDF

**Exemplo de uso:**
```
projetos/compliance/auditoria-q1-2026/
└── Kiro carrega automaticamente compliance.md
```

---

### 4. `comercial.md`
**Quando é usado:** Projetos na pasta `projetos/comercial/**`

**Diretrizes:**
- Linguagem persuasiva e orientada a valor
- Foco em benefícios para o cliente
- Estrutura de proposta comercial
- Conversão automática para Word + PowerPoint (se aplicável)

**Exemplo de uso:**
```
projetos/comercial/proposta-cliente-y/
└── Kiro carrega automaticamente comercial.md
```

---

## 🔧 Como Funcionam

### 1. Detecção Automática
```
Usuário cria projeto em: projetos/juridico/contrato-abc/
                                    ↓
Kiro detecta palavra "juridico" no caminho
                                    ↓
Kiro carrega steering-files/juridico.md automaticamente
                                    ↓
Todas as diretrizes são aplicadas
```

### 2. Configuração no Steering File
```markdown
---
inclusion: fileMatch
fileMatchPattern: "projetos/juridico/**"
---

# Diretrizes para Time Jurídico
...
```

### 3. Aplicação das Diretrizes
- Kiro lê o steering file antes de gerar qualquer documento
- Aplica padrões de linguagem, estrutura e formatação
- Executa conversões automáticas conforme especificado
- Registra logs de auditoria

---

## 📝 Estrutura de um Steering File

```markdown
---
inclusion: fileMatch
fileMatchPattern: "projetos/<area>/**"
---

# Diretrizes para Time <Área>

## Contexto
Breve descrição do contexto e objetivo

## Padrões de Documentos
- Padrão 1
- Padrão 2
- Padrão 3

## Conversão Automática
Instruções de conversão:
1. Converter para Word
2. Converter para PDF
3. Salvar em pasta específica

## Estrutura de Saída
Exemplo de estrutura de pastas

## Checklist Pós-Geração
- [ ] Item 1
- [ ] Item 2
- [ ] Item 3
```

---

## 🔍 Exemplos de Diretrizes

### Linguagem Formal (Jurídico)
```markdown
## Padrões de Linguagem
- Usar "o Contratante" e "o Contratado" (com maiúsculas)
- Evitar contrações ("não" ao invés de "n")
- Numerar todas as cláusulas
- Incluir definições no início
```

### Linguagem Acolhedora (RH)
```markdown
## Padrões de Linguagem
- Usar linguagem inclusiva (colaborador/colaboradora)
- Tom positivo e encorajador
- Evitar jargões técnicos
- Incluir exemplos práticos
```

### Linguagem Técnica (Compliance)
```markdown
## Padrões de Linguagem
- Objetividade e precisão
- Referenciar normas e regulamentos
- Incluir evidências e anexos
- Estrutura: Contexto → Análise → Conclusão → Recomendações
```

### Linguagem Persuasiva (Comercial)
```markdown
## Padrões de Linguagem
- Foco em benefícios, não em features
- Usar dados e métricas
- Incluir cases de sucesso
- Call-to-action claro
```

---

## 🚀 Fluxo Completo

### Exemplo: Criação de Contrato

```
1. Usuário cria pasta:
   projetos/juridico/contrato-cliente-x/

2. Usuário adiciona referências:
   projetos/juridico/contrato-cliente-x/entrada/
   ├── contratos-similares/
   ├── template-base.docx
   └── briefing.txt

3. Usuário pede ao Kiro:
   "Crie um contrato de prestação de serviços para Cliente X"

4. Kiro:
   - Detecta pasta "juridico"
   - Carrega steering-files/juridico.md
   - Lê todos os arquivos de entrada
   - Gera contrato.md seguindo diretrizes
   - Executa conversões automáticas:
     * python ferramentas/conversao-word-e-pdf/md_para_word.py contrato.md --template juridico
     * python ferramentas/conversao-word-e-pdf/md_para_pdf.py contrato.md
   - Salva em pasta-saida/

5. Resultado:
   projetos/juridico/contrato-cliente-x/saida/
   ├── contrato-cliente-x.md
   ├── contrato-cliente-x.docx
   └── contrato-cliente-x.pdf
```
**Última atualização:** 2026-01-24  
**Versão:** 1.0  
**Autor:** Projeto Kiro para Não-Dev
