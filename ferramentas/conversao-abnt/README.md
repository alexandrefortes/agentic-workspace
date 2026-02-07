# 📄 Conversor Markdown para ABNT (LaTeX)

Ferramenta para converter automaticamente documentos escritos em Markdown para PDF formatado nas normas da ABNT (padrão TCC UFOP), utilizando LaTeX como base.

## 🚀 Funcionalidades

-   **Conversão Automática**: Transforma arquivos `.md` em `.tex`.
-   **Padrão ABNT**: Utiliza o template aprovado (abnTeX2) com as customizações da UFOP (Capa, Folha de Rosto, etc.).
-   **Figuras**: Suporte para inclusão de imagens.
-   **Referências**: Suporte para citações e referências bibliográficas (via `biblatex`).

## 📦 Como Usar

### 1. Estrutura da Pasta de Entrada

Crie uma pasta para o seu conteúdo (ex: `meu-tcc`) e organize os arquivos `.md` em ordem alfabética, pois eles serão compilados nessa sequência.

Exemplo:
```text
meu-tcc/
├── 01-introducao.md
├── 02-desenvolvimento.md
├── 03-conclusao.md
└── figuras/
    ├── grafico1.png
    └── esquema.jpg
```

### 2. Executando a Conversão

Abra o terminal e execute o script `converter.py` passando a pasta de entrada:

```bash
python ferramentas/conversao-abnt/converter.py "caminho/para/meu-tcc" --output "meu-tcc-final.pdf"
```

O PDF final será gerado no caminho especificado.

## 📝 Escrevendo em Markdown para ABNT

### Capítulos e Seções
Use os níveis de título do Markdown:
```markdown
# Introdução (Vira Capítulo)
## Objetivo (Vira Seção)
### Específicos (Vira Subseção)
```

### Figuras
Use a sintaxe padrão de imagens do Markdown. **Importante**: Coloque as imagens na pasta `figuras` dentro da sua pasta de conteúdo.
```markdown
![Legenda da Imagem](figuras/minha-imagem.png)
```

### Citações (Avançado)
Se precisar citar, use o formato do Pandoc (`@chave-da-referencia`) e garanta que o arquivo `.bib` esteja configurado no template.

## ⚙️ Detalhes Técnicos

-   **Backend**: LuaLaTeX + Pandoc.
-   **Template**: O arquivo `template_main.tex` em `template/` define a estrutura.
-   **Build**: O script cria uma pasta `_build` temporária para compilação.

## ⚠️ Requisitos do Sistema

O template LaTeX utiliza a classe `memoir` em versões recentes, que requer um kernel LaTeX atualizado (2023+). Se você receber o erro `Your LaTeX release is too old`, atualize sua instalação do MiKTeX ou TeX Live.
