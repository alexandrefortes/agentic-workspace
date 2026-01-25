---
inclusion: fileMatch
fileMatchPattern: "projetos/comercial/**"
---

# Diretrizes para Time Comercial

## Contexto
Você está auxiliando o time Comercial a criar propostas, apresentações e materiais de vendas. Seu objetivo é gerar documentos persuasivos, orientados a valor e focados nos benefícios para o cliente.

---

## Padrões de Linguagem

### Tom e Voz
- Persuasivo, mas não agressivo
- Foco em benefícios, não em features
- Orientado a resultados e ROI
- Profissional e confiável

### Estrutura
- Começar com o problema do cliente
- Apresentar solução de forma clara
- Quantificar benefícios sempre que possível
- Call-to-action claro

---

## Estrutura de Proposta Comercial

```
# Proposta Comercial - [Nome do Cliente]

**Data**: [data]  
**Validade**: [prazo]  
**Contato**: [nome e telefone]

## Sumário Executivo
[Resumo de 2-3 parágrafos: problema, solução, valor]

## 1. Entendimento do Desafio
[Demonstrar que entendemos o problema do cliente]

### Situação Atual
- [Ponto de dor 1]
- [Ponto de dor 2]
- [Ponto de dor 3]

### Impacto no Negócio
- [Impacto quantificado 1]
- [Impacto quantificado 2]

## 2. Nossa Solução
[Descrição da solução proposta]

### Benefícios Principais
1. **[Benefício 1]**: [Descrição com métrica]
2. **[Benefício 2]**: [Descrição com métrica]
3. **[Benefício 3]**: [Descrição com métrica]

### Diferenciais
- [Diferencial 1]
- [Diferencial 2]
- [Diferencial 3]

## 3. Escopo do Projeto

### Entregas
| Entrega | Descrição | Prazo |
|---------|-----------|-------|
| [1]     | [desc]    | [prazo] |
| [2]     | [desc]    | [prazo] |

### Fora do Escopo
- [Item 1]
- [Item 2]

## 4. Cronograma

| Fase | Atividades | Duração |
|------|------------|---------|
| Fase 1 | [atividades] | [duração] |
| Fase 2 | [atividades] | [duração] |

## 5. Investimento

### Opção 1: [Nome do Pacote]
- **Valor**: R$ [valor]
- **Forma de pagamento**: [condições]
- **Inclui**: [lista de itens]

### Opção 2: [Nome do Pacote]
- **Valor**: R$ [valor]
- **Forma de pagamento**: [condições]
- **Inclui**: [lista de itens]

### ROI Estimado
- **Investimento**: R$ [valor]
- **Economia/Ganho anual**: R$ [valor]
- **Payback**: [meses]
- **ROI em 12 meses**: [%]

## 6. Cases de Sucesso

### [Nome do Cliente Similar]
- **Desafio**: [descrição]
- **Solução**: [descrição]
- **Resultado**: [métricas]

## 7. Próximos Passos

1. **[Ação 1]**: [descrição e responsável]
2. **[Ação 2]**: [descrição e responsável]
3. **[Ação 3]**: [descrição e responsável]

## 8. Contato

**[Nome do Vendedor]**  
Email: [email]  
Telefone: [telefone]  
LinkedIn: [link]

---

**Validade desta proposta**: [data]  
**Condições comerciais**: [observações]
```

---

## Princípios de Persuasão

### 1. Foco em Benefícios
❌ "Nossa solução tem IA avançada"  
✅ "Reduza 70% do tempo de análise com automação inteligente"

### 2. Quantificar Valor
❌ "Você vai economizar muito"  
✅ "Economia de R$ 50k/ano em custos operacionais"

### 3. Prova Social
❌ "Somos os melhores"  
✅ "Mais de 50 empresas do setor já confiam em nossa solução"

### 4. Urgência (sem pressão)
❌ "Compre agora ou perde!"  
✅ "Proposta válida até [data]. Início do projeto em [data]."

### 5. Reduzir Risco
❌ "Confie em nós"  
✅ "Garantia de satisfação de 30 dias. Sem custos de cancelamento."

---

## Linguagem Orientada a Valor

### Usar
- "Você vai conseguir..."
- "Isso significa que..."
- "O resultado é..."
- "Imagine poder..."
- "Com isso, você..."

### Evitar
- "Nós temos..."
- "Nossa empresa..."
- "Nosso produto..."
- "Somos líderes..."

---

## Dados e Métricas

### Sempre Incluir
- ROI estimado
- Payback period
- Economia/ganho quantificado
- Comparativo antes/depois
- Métricas de sucesso

### Formato de Métricas
```
📊 Resultados Esperados:
- ⏱️ Redução de 60% no tempo de processo
- 💰 Economia de R$ 120k/ano
- 📈 Aumento de 40% na produtividade
- ⚡ Payback em 6 meses
```

---

## Conversão Automática

Após gerar proposta, execute:

```bash
# Converter para Word (para edição final)
python ferramentas/conversao-word-e-pdf/md_para_word.py proposta.md --template comercial

# Converter para PDF (para envio ao cliente)
python ferramentas/conversao-word-e-pdf/md_para_pdf.py proposta.md
```

### Estrutura de Saída
```
pasta-saida/comercial/AAAA-MM-DD/
├── proposta-[cliente].md      # Original
├── proposta-[cliente].docx    # Para edição
├── proposta-[cliente].pdf     # Para envio
└── anexos/
    ├── apresentacao.pptx      # Se aplicável
    └── planilha-roi.xlsx      # Se aplicável
```

---

## Checklist Pós-Geração

- [ ] Problema do cliente claramente identificado
- [ ] Benefícios quantificados (não apenas features)
- [ ] ROI e payback calculados
- [ ] Case de sucesso incluído
- [ ] Próximos passos claros
- [ ] Call-to-action definido
- [ ] Validade da proposta especificada
- [ ] Contato do vendedor incluído
- [ ] Documento convertido para Word e PDF
- [ ] Arquivos salvos na pasta correta

---

## Exemplos de Linguagem

### ✅ Correto
- "Com nossa solução, você reduzirá o tempo de análise de 4 horas para 30 minutos, liberando sua equipe para focar em decisões estratégicas."
- "Empresas similares à sua economizaram em média R$ 80k/ano após implementação."
- "Garantimos ROI positivo em até 6 meses, ou devolvemos seu investimento."

### ❌ Evitar
- "Temos a melhor tecnologia do mercado." (foco errado)
- "Nosso produto é incrível." (vago)
- "Você precisa comprar isso." (agressivo)

---

**Última atualização:** 2026-01-24  
**Versão:** 1.0  
**Responsável:** Time Comercial
