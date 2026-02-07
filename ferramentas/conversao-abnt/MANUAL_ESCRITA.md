# Guia de Escrita: Markdown para ABNT

Este guia explica como escrever seus textos em formato **Markdown** para que nossa ferramenta os converta corretamente para um PDF nas normas ABNT da UFOP.

## 1. Títulos e Seções

A estrutura do seu trabalho é definida pelos títulos. Evite pular níveis (ex: de Título 1 direto para Título 3).

```markdown
# Introdução (Nível 1 - Capítulo)
## Objetivos (Nível 2 - Seção)
### Objetivos Específicos (Nível 3 - Subseção)
```

## 2. Formatação de Texto

-   **Negrito**: Use dois asteriscos. Ex: `**texto importante**` → **texto importante**.
-   *Itálico*: Use um asterisco ou underline. Ex: `*estrangeirismo*` → *estrangeirismo*.
-   `Código`: Use crases. Ex: ` `variavel` ` → `variavel`.

## 3. Citações Diretas

Para citações longas (mais de 3 linhas), que devem ter recuo no PDF, use o sinal de maior `>`:

```markdown
> A inteligência artificial generativa refere-se a modelos computacionais capazes de gerar novos dados... (Autor, Ano, p. 123)
```

O resultado no PDF será aquele parágrafo recuado com fonte menor, conforme a ABNT.

## 4. Listas

### Com marcadores
```markdown
-   Item um
-   Item dois
    -   Subitem
```

### Numeradas
```markdown
1.  Primeiro passo
2.  Segundo passo
```

## 5. Inserindo Imagens (Figuras)

Coloque suas imagens na pasta `figuras/` junto com seus arquivos Markdown.

Use o formato padrão:
```markdown
![Legenda da figura explicativa](figuras/minha-imagem.png)
```

A ferramenta irá automaticamente:
1.  Centralizar a imagem.
2.  Colocar a legenda "Figura X - Legenda da figura explicativa".
3.  Adicionar à Lista de Figuras.

## 6. Tabelas

Você pode criar tabelas simples desenhando-as com barras verticais e traços:

```markdown
| Coluna 1 | Coluna 2 |
|----------|----------|
| Dado A   | Dado B   |
| Dado C   | Dado D   |
```

## 7. Notas de Rodapé

Para adicionar uma nota de rodapé, use um "chapéu" e colchetes. O texto da nota pode ficar em qualquer lugar (geralmente no final do parágrafo ou do arquivo), mas recomendamos colocar logo após o uso para não perder.

```markdown
O conceito de IA generativa[^1] tem crescido muito.

[^1]: Gartner define IA generativa como modelos que aprendem padrões...
```

## 8. Referências Bibliográficas

Se você estiver usando um arquivo de referências `.bib`, pode citar autores assim:

-   `@sobrenome2024` → (SOBRENOME, 2024)
-   `@sobrenome2024 diz que...` → Sobrenome (2024) diz que...

*Nota: Para isso funcionar, seu projeto precisa ter o arquivo `referencias.bib` configurado.*

## Exemplo Completo

```markdown
# Resultados

Analisamos **100 casos** de atendimento. Desses, a maioria foi resolvida rapidamente.

> O atendimento ao cliente é a alma do negócio. (SILVA, 2020)

## Análise Quantitativa

| Categoria | Quantidade |
|-----------|------------|
| Suporte   | 50         |
| Vendas    | 30         |
| Outros    | 20         |

Conforme a imagem abaixo:

![Gráfico de pizza dos atendimentos](figuras/grafico-pizza.png)
```
