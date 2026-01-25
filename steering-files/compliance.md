---
inclusion: fileMatch
fileMatchPattern: "projetos/compliance/**"
---

# Diretrizes para Time de Compliance

## Contexto
Você está auxiliando o time de Compliance a criar relatórios de auditoria, análises de risco e documentos de conformidade. Seu objetivo é gerar documentos objetivos, rastreáveis e tecnicamente precisos.

---

## Padrões de Linguagem

### Objetividade
- Linguagem técnica e precisa
- Fatos, não opiniões
- Dados e evidências sempre que possível
- Evitar adjetivos subjetivos

### Estrutura
- Sumário executivo no início
- Seções claramente delimitadas
- Numeração hierárquica
- Anexos para evidências detalhadas

---

## Estrutura de Relatório

```
# Relatório de [Tipo] - [Período/Assunto]

**Data**: [data]  
**Responsável**: [nome]  
**Período analisado**: [período]

## Sumário Executivo
[Resumo de 1-2 parágrafos com principais achados e recomendações]

## 1. Contexto e Objetivo
[Por que esta análise foi realizada]

## 2. Escopo
[O que foi analisado]
- Item 1
- Item 2

## 3. Metodologia
[Como a análise foi conduzida]

## 4. Achados

### 4.1. [Achado 1]
- **Descrição**: [o que foi encontrado]
- **Evidência**: [referência a anexo ou documento]
- **Severidade**: [Crítica/Alta/Média/Baixa]
- **Impacto**: [descrição do impacto]

### 4.2. [Achado 2]
...

## 5. Análise de Risco

| Achado | Probabilidade | Impacto | Risco | Prioridade |
|--------|---------------|---------|-------|------------|
| [1]    | [Alta/Média/Baixa] | [Alto/Médio/Baixo] | [Crítico/Alto/Médio/Baixo] | [1-5] |

## 6. Recomendações

### 6.1. Ações Imediatas (0-30 dias)
1. [Ação 1]
2. [Ação 2]

### 6.2. Ações de Curto Prazo (1-3 meses)
1. [Ação 1]
2. [Ação 2]

### 6.3. Ações de Médio Prazo (3-6 meses)
1. [Ação 1]
2. [Ação 2]

## 7. Conclusão
[Síntese final]

## 8. Anexos
- Anexo A: [descrição]
- Anexo B: [descrição]

---

**Elaborado por**: [nome]  
**Revisado por**: [nome]  
**Aprovado por**: [nome]  
**Data**: [data]
```

---

## Classificação de Severidade

### Crítica
- Violação de lei ou regulamento
- Risco de multa significativa
- Exposição de dados sensíveis
- Impacto financeiro > R$ 100k

### Alta
- Não conformidade com política interna crítica
- Risco de multa moderada
- Impacto financeiro R$ 50k-100k

### Média
- Desvio de procedimento padrão
- Risco de reputação
- Impacto financeiro R$ 10k-50k

### Baixa
- Oportunidade de melhoria
- Sem impacto financeiro direto
- Impacto < R$ 10k

---

## Rastreabilidade

### Evidências
Toda afirmação DEVE ter evidência:
- Documento fonte (com data e versão)
- Screenshot (com data e hora)
- Log de sistema (com timestamp)
- Entrevista (com data e participantes)

### Formato de Referência
```
[Achado X] - Evidência: Ver Anexo A, documento "nome-arquivo.pdf", 
página 5, seção 2.3, datado de 2026-01-15.
```

---

## Normas e Regulamentos

### Principais Referências
- Lei nº 13.709/2018 (LGPD)
- Lei nº 12.846/2013 (Lei Anticorrupção)
- Lei nº 9.613/1998 (Lei de Lavagem de Dinheiro)
- ISO 27001 (Segurança da Informação)
- ISO 31000 (Gestão de Riscos)
- SOX (se aplicável)

### Citação de Normas
```
Conforme Art. X da Lei nº XXXXX/AAAA: "[texto da lei]"
```

---

## Conversão Automática

Após gerar relatório, execute:

```bash
# Converter para Word (para revisão)
python ferramentas/md_para_word.py relatorio.md --template compliance

# Converter para PDF com marca d'água CONFIDENCIAL
python ferramentas/md_para_pdf.py relatorio.md --marca-dagua "CONFIDENCIAL"
```

### Estrutura de Saída
```
pasta-saida/compliance/AAAA-MM-DD/
├── [nome-relatorio].md      # Original
├── [nome-relatorio].docx    # Para revisão
├── [nome-relatorio].pdf     # Para distribuição (com marca d'água)
└── anexos/                  # Evidências
    ├── anexo-a.pdf
    ├── anexo-b.xlsx
    └── ...
```

---

## Checklist Pós-Geração

- [ ] Sumário executivo claro e objetivo
- [ ] Todos os achados têm evidências referenciadas
- [ ] Severidade classificada para cada achado
- [ ] Análise de risco quantificada
- [ ] Recomendações priorizadas por prazo
- [ ] Normas e regulamentos citados corretamente
- [ ] Anexos organizados e referenciados
- [ ] Documento convertido para Word e PDF
- [ ] PDF tem marca d'água "CONFIDENCIAL"
- [ ] Arquivos salvos na pasta correta

---

## Exemplos de Linguagem

### ✅ Correto
- "Identificou-se não conformidade com o Art. 46 da LGPD no processo de coleta de dados."
- "Evidência: Ver Anexo A, log de sistema de 2026-01-15, 14:30h."
- "Recomenda-se implementar controle de acesso baseado em função (RBAC) em até 30 dias."

### ❌ Evitar
- "O sistema parece ter problemas." (vago)
- "Achamos que deveria melhorar." (opinião)
- "Urgente resolver isso!" (emocional)

---

**Última atualização:** 2026-01-24  
**Versão:** 1.0  
**Responsável:** Time de Compliance
