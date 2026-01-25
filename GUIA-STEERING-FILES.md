# 📘 Guia: Steering Files para Conversão de Documentos

## O que são Steering Files?

Steering files são arquivos de contexto que instruem o Kiro (ou outros agentes de IA) sobre como se comportar em determinadas situações. Eles são carregados automaticamente e influenciam todas as interações do agente.

---

## Por que Steering Files são a Melhor Opção?

### ✅ Vantagens

1. **Contexto Sempre Disponível**
   - O agente sempre sabe como converter documentos
   - Não precisa perguntar ao usuário como fazer
   - Comportamento consistente em todas as sessões

2. **Automação Inteligente**
   - Quando o usuário pede "gere um PDF", o agente sabe exatamente qual script usar
   - Não precisa de instruções manuais a cada vez
   - Reduz erros e inconsistências

3. **Manutenção Centralizada**
   - Atualizar o steering file atualiza o comportamento em todos os projetos
   - Fácil de versionar e documentar
   - Equipe inteira usa o mesmo padrão

4. **Flexibilidade**
   - Pode incluir regras condicionais
   - Pode especificar diferentes comportamentos por tipo de documento
   - Pode incluir troubleshooting e fallbacks

### ❌ Alternativas Menos Eficientes

**Opção 1: Instruir manualmente a cada vez**
- ❌ Usuário precisa lembrar dos comandos
- ❌ Inconsistente (cada pessoa faz diferente)
- ❌ Propenso a erros

**Opção 2: Documentação separada**
- ❌ Agente não lê automaticamente
- ❌ Usuário precisa consultar e copiar comandos
- ❌ Documentação pode ficar desatualizada

**Opção 3: Scripts wrapper**
- ❌ Mais complexo de manter
- ❌ Menos flexível
- ❌ Agente ainda precisa saber quando usar

---

## Estrutura do Steering File Ideal

### Front Matter (Metadados)

```markdown
---
inclusion: always
---
```

**Opções de `inclusion`:**
- `always` - Sempre incluído (recomendado para conversão de documentos)
- `fileMatch` - Incluído apenas quando certos arquivos são abertos
- `manual` - Incluído apenas quando usuário referencia com `#`

### Seções Recomendadas

1. **Instruções Claras e Diretas**
   - Use linguagem imperativa: "DEVE usar", "SEMPRE faça"
   - Seja específico sobre comandos e caminhos

2. **Exemplos Práticos**
   - Mostre comandos completos
   - Inclua casos de uso comuns
   - Demonstre diferentes opções

3. **Regras de Quando Usar**
   - Especifique gatilhos (ex: "quando o usuário pedir PDF")
   - Defina exceções (ex: "quando NÃO usar")

4. **Troubleshooting Básico**
   - Erros comuns e soluções
   - Como verificar se ferramentas estão instaladas
   - Onde encontrar documentação completa

5. **Fluxo de Trabalho**
   - Passo a passo do que fazer
   - Formato de resposta ao usuário
   - Como reportar sucesso/erro

---

## Exemplo: Nosso Steering File

Veja `.kiro/steering/ideias.md` para o exemplo completo implementado.

### Estrutura Aplicada

```markdown
---
inclusion: always
---

# Título Descritivo

## Seção 1: Regras Básicas
[Regras de nomenclatura, etc.]

## Seção 2: Conversão de Documentos
### Scripts Disponíveis
[Lista de scripts]

### Como Usar
[Comandos com exemplos]

### Regras Importantes
[Lista numerada de regras imperativas]

### Fluxo de Trabalho Recomendado
[Passo a passo]

### Troubleshooting Rápido
[Soluções para problemas comuns]

## Seção 3: Exemplos de Uso Comum
[Casos práticos com comandos completos]

## Seção 4: Quando NÃO Usar
[Exceções e casos especiais]

## Resumo
[Checklist rápido com ✅ e ❌]
```

---

## Boas Práticas

### ✅ Faça

1. **Use linguagem imperativa**
   ```markdown
   ✅ "Você DEVE usar os scripts do projeto"
   ❌ "Você pode usar os scripts do projeto"
   ```

2. **Seja específico com comandos**
   ```markdown
   ✅ python ferramentas/md_para_word.py arquivo.md
   ❌ Use o script de conversão
   ```

3. **Inclua exemplos completos**
   ```markdown
   ✅ Mostrar comando + saída esperada
   ❌ Apenas mencionar que existe um script
   ```

4. **Defina o fluxo de trabalho**
   ```markdown
   ✅ "1. Criar MD, 2. Converter Word, 3. Converter PDF"
   ❌ "Converta os arquivos conforme necessário"
   ```

5. **Use formatação visual**
   ```markdown
   ✅ Usar ✅ ❌ 📝 🔧 para destacar
   ❌ Apenas texto corrido
   ```

### ❌ Evite

1. **Linguagem vaga ou opcional**
   - "Você pode considerar..."
   - "Talvez seja bom..."
   - "Se quiser..."

2. **Instruções incompletas**
   - Comandos sem caminhos completos
   - Exemplos sem contexto
   - Referências a documentação externa sem link

3. **Excesso de informação**
   - Documentação técnica completa (deixe para README)
   - Histórico de decisões
   - Detalhes de implementação

4. **Falta de priorização**
   - Todas as opções parecem igualmente importantes
   - Sem indicação de "caminho feliz"
   - Sem hierarquia de informação

---

## Como Testar o Steering File

### Teste 1: Conversão Básica
**Comando do usuário:**
> "Crie um documento sobre política de férias e gere o Word"

**Comportamento esperado:**
1. Agente cria `politica-de-ferias.md`
2. Agente executa `python ferramentas/md_para_word.py politica-de-ferias.md`
3. Agente informa sucesso e tamanho do arquivo

### Teste 2: Conversão com Template
**Comando do usuário:**
> "Crie um contrato de prestação de serviços em Word"

**Comportamento esperado:**
1. Agente cria `contrato-prestacao-servicos.md`
2. Agente executa com template: `python ferramentas/md_para_word.py contrato-prestacao-servicos.md --template juridico`
3. Agente informa sucesso

### Teste 3: Conversão Múltipla
**Comando do usuário:**
> "Crie uma proposta comercial em Word e PDF"

**Comportamento esperado:**
1. Agente cria `proposta-comercial.md`
2. Agente executa conversão Word com template comercial
3. Agente executa conversão PDF
4. Agente lista todos os arquivos gerados

### Teste 4: Troubleshooting
**Comando do usuário:**
> "Gere o PDF mas deu erro de Pandoc não encontrado"

**Comportamento esperado:**
1. Agente consulta seção de troubleshooting do steering file
2. Agente sugere verificar instalação: `pandoc --version`
3. Agente sugere configurar PATH ou consultar `ferramentas/README.md`

---

## Manutenção do Steering File

### Quando Atualizar

1. **Novos scripts adicionados**
   - Adicionar à seção "Scripts Disponíveis"
   - Incluir exemplos de uso

2. **Novos templates criados**
   - Adicionar à lista de templates
   - Incluir caso de uso

3. **Problemas comuns identificados**
   - Adicionar à seção de troubleshooting
   - Incluir solução testada

4. **Mudanças nos caminhos/comandos**
   - Atualizar todos os exemplos
   - Testar novamente

### Versionamento

Mantenha o steering file no Git junto com o projeto:
```bash
git add .kiro/steering/ideias.md
git commit -m "docs: atualizar steering file com novos templates"
```

---

## Comparação: Com vs Sem Steering File

### Sem Steering File

**Usuário:** "Crie um contrato em Word"

**Agente:** "Criei o arquivo contrato.md. Para converter para Word, você pode usar ferramentas como Pandoc ou LibreOffice."

**Usuário:** "Como uso o Pandoc?"

**Agente:** "Execute: `pandoc contrato.md -o contrato.docx`"

**Usuário:** "Deu erro, Pandoc não encontrado"

**Agente:** "Você precisa instalar o Pandoc primeiro..."

❌ **Resultado:** Múltiplas interações, frustração, inconsistência

---

### Com Steering File

**Usuário:** "Crie um contrato em Word"

**Agente:** "Criei o contrato e converti para Word usando o template jurídico:

✅ Arquivos gerados:
- contrato-prestacao-servicos.md (original)
- contrato-prestacao-servicos.docx (18.5 KB)

Comando executado:
`python ferramentas/md_para_word.py contrato-prestacao-servicos.md --template juridico`"

✅ **Resultado:** Uma interação, sucesso imediato, padrão corporativo aplicado

---

## Conclusão

Steering files são a melhor forma de instruir o Kiro sobre conversão de documentos porque:

1. ✅ **Automático** - Sempre disponível, sem necessidade de instruções manuais
2. ✅ **Consistente** - Mesmo comportamento em todas as sessões
3. ✅ **Manutenível** - Fácil de atualizar e versionar
4. ✅ **Escalável** - Funciona para toda a equipe
5. ✅ **Inteligente** - Agente toma decisões corretas automaticamente

O steering file `.kiro/steering/ideias.md` implementa todas essas boas práticas e está pronto para uso!

---

**Próximos Passos:**

1. ✅ Steering file criado e documentado
2. 📝 Testar com casos de uso reais
3. 🔄 Iterar baseado no feedback
4. 📚 Criar steering files para outras áreas (jurídico, RH, compliance)

---

**Referências:**
- `.kiro/steering/ideias.md` - Steering file implementado
- `ferramentas/README.md` - Documentação técnica completa
- `RELATORIO-CONFIGURACAO.md` - Status da configuração do ambiente
