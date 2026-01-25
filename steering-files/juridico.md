---
inclusion: fileMatch
fileMatchPattern: "projetos/juridico/**"
---

# Diretrizes para Time Jurídico

## Contexto
Você está auxiliando o time Jurídico da empresa a criar documentos legais (contratos, pareceres, análises). Seu objetivo é gerar documentos tecnicamente corretos, formalmente adequados e em conformidade com a legislação brasileira.

---

## Padrões de Linguagem

### Formalidade
- Usar linguagem formal e técnica
- Evitar contrações: "não" ao invés de "não há"
- Usar terceira pessoa: "o Contratante", "o Contratado"
- Capitalizar partes: "Contratante", "Contratado", "Partes"

### Estrutura de Frases
- Frases claras e objetivas
- Evitar ambiguidades
- Usar conectivos formais: "outrossim", "destarte", "doravante"
- Numerar todas as cláusulas e subcláusulas

### Terminologia
- Usar termos jurídicos corretos
- Definir termos técnicos no início do documento
- Manter consistência terminológica

---

## Cláusulas Obrigatórias

Todo contrato DEVE incluir:

### 1. Qualificação das Partes
```
CONTRATANTE: [Nome completo], [nacionalidade], [estado civil], [profissão],
portador do CPF nº [número], residente e domiciliado em [endereço completo].

CONTRATADO: [Nome completo], [nacionalidade], [estado civil], [profissão],
portador do CPF nº [número], residente e domiciliado em [endereço completo].
```

### 2. Objeto do Contrato
- Descrição clara e detalhada
- Escopo bem definido
- Exclusões explícitas (se aplicável)

### 3. Prazo e Vigência
- Data de início
- Data de término ou condições de término
- Renovação automática (se aplicável)

### 4. Valor e Forma de Pagamento
- Valor total ou forma de cálculo
- Parcelas e vencimentos
- Forma de pagamento
- Reajustes (se aplicável)

### 5. Proteção de Dados (LGPD)
```
CLÁUSULA X - PROTEÇÃO DE DADOS PESSOAIS

As Partes declaram conhecer e se comprometem a cumprir integralmente as
disposições da Lei nº 13.709/2018 (Lei Geral de Proteção de Dados - LGPD),
especialmente no que se refere ao tratamento de dados pessoais.

X.1. O CONTRATADO compromete-se a:
a) Tratar dados pessoais apenas para as finalidades previstas neste Contrato;
b) Implementar medidas de segurança técnicas e administrativas adequadas;
c) Não compartilhar dados pessoais com terceiros sem autorização prévia;
d) Notificar o CONTRATANTE em até 24 horas sobre qualquer incidente de segurança.

X.2. O CONTRATADO será responsável por quaisquer danos causados por violação
à LGPD, incluindo multas, indenizações e custos de remediação.
```

### 6. Confidencialidade
- Definição de informações confidenciais
- Obrigações de sigilo
- Exceções ao sigilo
- Prazo de confidencialidade

### 7. Rescisão
- Condições de rescisão
- Prazos de aviso prévio
- Consequências da rescisão
- Devolução de materiais/informações

### 8. Foro
```
CLÁUSULA X - FORO

Fica eleito o foro da Comarca de São Paulo, Estado de São Paulo, para dirimir
quaisquer dúvidas ou controvérsias oriundas deste Contrato, com renúncia
expressa a qualquer outro, por mais privilegiado que seja.
```

---

## Numeração de Cláusulas

### Formato Padrão
```
CLÁUSULA 1 - OBJETO
1.1. Subcláusula
1.2. Subcláusula
    1.2.1. Item
    1.2.2. Item

CLÁUSULA 2 - PRAZO
2.1. Subcláusula
...
```

### Regras
- Cláusulas principais em MAIÚSCULAS
- Subcláusulas numeradas (1.1, 1.2, etc.)
- Itens com letras (a, b, c) ou números (1.2.1, 1.2.2)

---

## Estrutura de Documento

### Contratos
```
CONTRATO DE [TIPO]

CONTRATANTE: [qualificação]
CONTRATADO: [qualificação]

As Partes acima qualificadas têm, entre si, justo e acertado o presente
Contrato de [tipo], que se regerá pelas cláusulas seguintes:

CLÁUSULA 1 - OBJETO
...

CLÁUSULA 2 - PRAZO
...

[demais cláusulas]

E, por estarem assim justos e contratados, firmam o presente instrumento em
2 (duas) vias de igual teor e forma, na presença das testemunhas abaixo.

São Paulo, [data por extenso].

_______________________________
CONTRATANTE

_______________________________
CONTRATADO

TESTEMUNHAS:

_______________________________
Nome:
CPF:

_______________________________
Nome:
CPF:
```

### Pareceres
```
PARECER JURÍDICO Nº [número]/[ano]

INTERESSADO: [nome]
ASSUNTO: [descrição breve]
DATA: [data]

I - RELATÓRIO
[Contexto e fatos relevantes]

II - FUNDAMENTAÇÃO
[Análise jurídica com base em legislação, doutrina e jurisprudência]

III - CONCLUSÃO
[Opinião jurídica fundamentada]

São Paulo, [data por extenso].

_______________________________
[Nome do Advogado]
OAB/SP nº [número]
```

---

## Conversão Automática

Após gerar qualquer documento em Markdown, você DEVE executar:

### 1. Conversão para Word
```bash
python ferramentas/md_para_word.py documento.md --template juridico
```

### 2. Conversão para PDF Assinável
```bash
python ferramentas/md_para_pdf.py documento.md --assinavel
```

### 3. Estrutura de Saída
```
pasta-saida/juridico/AAAA-MM-DD/
├── [nome-documento].md      # Original em Markdown
├── [nome-documento].docx    # Para revisão e edição
└── [nome-documento].pdf     # Para assinatura digital
```

---

## Checklist Pós-Geração

Antes de entregar o documento, verifique:

- [ ] Todas as partes estão qualificadas corretamente
- [ ] Objeto do contrato está claro e detalhado
- [ ] Prazo e vigência estão definidos
- [ ] Valores e forma de pagamento estão especificados
- [ ] Cláusula de proteção de dados (LGPD) está incluída
- [ ] Cláusula de confidencialidade está incluída
- [ ] Condições de rescisão estão claras
- [ ] Foro está definido (São Paulo/SP)
- [ ] Todas as cláusulas estão numeradas corretamente
- [ ] Documento foi convertido para Word e PDF
- [ ] Arquivos foram salvos na pasta correta

---

## Referências Legais

### Legislação Aplicável
- Lei nº 10.406/2002 (Código Civil)
- Lei nº 13.709/2018 (LGPD)
- Lei nº 8.078/1990 (Código de Defesa do Consumidor)
- Lei nº 13.874/2019 (Declaração de Direitos de Liberdade Econômica)

### Jurisprudência
- Consultar STJ e STF para temas relevantes
- Citar súmulas quando aplicável

---

## Exemplos de Linguagem

### ✅ Correto
- "O Contratante obriga-se a efetuar o pagamento até o dia 10 de cada mês."
- "As Partes elegem o foro da Comarca de São Paulo."
- "Fica vedada a cessão deste Contrato sem anuência prévia e por escrito."

### ❌ Evitar
- "A empresa vai pagar até dia 10." (informal)
- "Qualquer problema vai ser resolvido em São Paulo." (vago)
- "Não pode passar o contrato pra outra pessoa." (coloquial)

---

## Observações Importantes

1. **Sempre revisar com advogado**: Documentos gerados são rascunhos e devem ser revisados por profissional habilitado.

2. **Adaptar ao caso concreto**: Cada situação é única. Adapte as cláusulas conforme necessário.

3. **Atualização legislativa**: Verifique se há legislação mais recente aplicável.

4. **Consultar precedentes**: Para casos complexos, consulte contratos similares já aprovados.

---

**Última atualização:** 2026-01-24  
**Versão:** 1.0  
**Responsável:** Time Jurídico
