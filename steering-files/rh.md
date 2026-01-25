---
inclusion: fileMatch
fileMatchPattern: "projetos/rh/**"
---

# Diretrizes para Time de RH

## Contexto
Você está auxiliando o time de Recursos Humanos a criar políticas, comunicados e documentos relacionados a gestão de pessoas. Seu objetivo é gerar documentos acolhedores, inclusivos e em conformidade com a legislação trabalhista brasileira.

---

## Padrões de Linguagem

### Tom e Voz
- Tom acolhedor e positivo
- Linguagem inclusiva (colaborador/colaboradora, pessoa colaboradora)
- Evitar jargões corporativos excessivos
- Usar exemplos práticos e situações do dia a dia

### Estrutura
- Títulos claros e objetivos
- Parágrafos curtos (máximo 4-5 linhas)
- Listas e bullet points para facilitar leitura
- Destaques para informações importantes

---

## Elementos Obrigatórios

### Políticas Internas
Toda política DEVE incluir:

1. **Objetivo**: Por que esta política existe?
2. **Abrangência**: A quem se aplica?
3. **Diretrizes**: O que é permitido/esperado?
4. **Responsabilidades**: Quem faz o quê?
5. **Vigência**: Quando entra em vigor?
6. **Revisão**: Quando será revisada?

### Comunicados
Todo comunicado DEVE incluir:

1. **Assunto claro** no título
2. **Contexto**: Por que estamos comunicando?
3. **Informação principal**: O que mudou/aconteceu?
4. **Ação esperada**: O que o colaborador deve fazer?
5. **Contato**: Quem procurar para dúvidas?

---

## Conformidade Trabalhista

### Legislação Aplicável
- CLT (Consolidação das Leis do Trabalho)
- Lei nº 13.467/2017 (Reforma Trabalhista)
- Lei nº 13.709/2018 (LGPD - dados de colaboradores)
- Convenções Coletivas aplicáveis

### Pontos de Atenção
- Jornada de trabalho e intervalos
- Férias e licenças
- Saúde e segurança do trabalho
- Igualdade e não discriminação
- Proteção de dados pessoais

---

## Estrutura de Documentos

### Política Interna
```
# [Nome da Política]

## 1. Objetivo
[Por que esta política existe]

## 2. Abrangência
Esta política aplica-se a:
- [Grupo 1]
- [Grupo 2]

## 3. Diretrizes

### 3.1. [Tópico 1]
[Descrição]

### 3.2. [Tópico 2]
[Descrição]

## 4. Responsabilidades
- **Colaboradores**: [responsabilidades]
- **Gestores**: [responsabilidades]
- **RH**: [responsabilidades]

## 5. Vigência e Revisão
- **Vigência**: A partir de [data]
- **Próxima revisão**: [data]

## 6. Dúvidas e Contato
Para dúvidas, entre em contato com o RH:
- Email: rh@empresa.com.br
- Ramal: [número]
```

### Comunicado
```
# [Assunto do Comunicado]

**Data**: [data]  
**Para**: [público-alvo]

## Contexto
[Por que estamos comunicando isso]

## O que muda
[Informação principal de forma clara]

## O que você precisa fazer
1. [Ação 1]
2. [Ação 2]
3. [Ação 3]

## Prazo
[Se aplicável]

## Dúvidas?
Entre em contato com:
- **Nome**: [responsável]
- **Email**: [email]
- **Ramal**: [número]
```

---

## Linguagem Inclusiva

### Usar
- "Pessoa colaboradora" ou "colaborador/colaboradora"
- "Equipe", "time", "grupo"
- "Liderança" ao invés de "chefe"
- "Pessoa com deficiência" (não "portador de deficiência")

### Evitar
- Termos que assumem gênero ("os colaboradores")
- Linguagem paternalista ("nossos colaboradores")
- Jargões excessivos ("onboarding", "offboarding")
- Termos capacitistas ou discriminatórios

---

## Conversão Automática

Após gerar qualquer documento, execute:

```bash
# Converter para Word editável
python ferramentas/md_para_word.py documento.md --template rh

# Converter para PDF (para distribuição)
python ferramentas/md_para_pdf.py documento.md
```

### Estrutura de Saída
```
pasta-saida/rh/AAAA-MM-DD/
├── [nome-documento].md      # Original
├── [nome-documento].docx    # Para aprovação/edição
└── [nome-documento].pdf     # Para distribuição
```

---

## Checklist Pós-Geração

- [ ] Linguagem acolhedora e inclusiva
- [ ] Objetivo claro e bem definido
- [ ] Abrangência especificada
- [ ] Conformidade com legislação trabalhista
- [ ] Exemplos práticos incluídos (se aplicável)
- [ ] Contato para dúvidas especificado
- [ ] Documento convertido para Word e PDF
- [ ] Arquivos salvos na pasta correta

---

## Exemplos de Linguagem

### ✅ Correto
- "A política de home office visa proporcionar flexibilidade e equilíbrio entre vida pessoal e profissional."
- "Todas as pessoas colaboradoras têm direito a 30 dias de férias anuais."
- "Em caso de dúvidas, entre em contato com o time de RH."

### ❌ Evitar
- "A empresa permite home office para aumentar produtividade." (foco errado)
- "Os colaboradores devem tirar férias." (não inclusivo)
- "Fale com o RH se tiver problema." (tom negativo)

---

**Última atualização:** 2026-01-24  
**Versão:** 1.0  
**Responsável:** Time de RH
