# PROGRAMA COMPUTACIONAL PARA PRÉ-DIMENSIONAMENTO E DIMENSIONAMENTO DE VIGAS DE CONCRETO ARMADO

> [!WARNING]
> Este projeto foi desenvolvido por estudantes no contexto de uma disciplina de graduação e possui finalidade exclusivamente educacional. Os resultados não foram necessariamente validados para uso profissional e devem ser utilizados com cautela e verificados independentemente.

## Descrição

O projeto aborda a dificuldade e o tempo necessário para realizar o pré-dimensionamento e o dimensionamento de vigas de concreto armado, especialmente devido à necessidade de executar cálculos repetitivos e verificar diferentes parâmetros. O objetivo é desenvolver um programa computacional com interface gráfica que automatize essas etapas, servindo principalmente como ferramenta de auxílio didático para estudantes e professores de Engenharia Civil, além de auxiliar profissionais da área.

As principais funcionalidades incluem a inserção de dados geométricos, propriedades dos materiais e carregamentos; o cálculo das armaduras longitudinais e transversais; a verificação dos limites normativos de armaduras e espaçamentos; e a geração de relatórios de cálculo em PDF.

## Instalação

Descreva os requisitos e os procedimentos necessários para instalar o projeto.

Por exemplo:

```bash
poetry install
````

## Uso

O usuário iniciará o programa e preencherá os campos da interface gráfica com os dados da viga, incluindo o vão, a largura da seção transversal, o cobrimento, a resistência do concreto, a classe do aço e os carregamentos atuantes. Com base no vão informado, o programa apresentará opções de altura para a viga. Após selecionar uma das opções, o usuário poderá executar o pré-dimensionamento e o dimensionamento à flexão e ao cisalhamento. O programa calculará as áreas de armadura longitudinal e transversal necessárias e verificará os limites normativos previstos no projeto. Ao final, os resultados serão apresentados na interface, com alertas para eventuais irregularidades, e poderão ser exportados em um relatório de cálculo em PDF.

# Exemplo de uso

Como exemplo de uso, o usuário poderá informar o vão da viga, definir sua largura e inserir as propriedades dos materiais e os carregamentos atuantes. O programa apresentará opções de altura compatíveis com o vão informado. Após selecionar uma delas, realizará os cálculos e apresentará as armaduras necessárias e as verificações normativas. O usuário também poderá selecionar outra altura sugerida e comparar os resultados obtidos.

## Exemplos

Descreva ou indique os exemplos disponíveis no diretório [`exemplos/`](exemplos/).

## Testes

Os testes automatizados estão no diretório [`tests/`](tests/).

Para executá-los:

```bash
poetry run pytest
```

## Estrutura do projeto

```text
.
├── src/
│   └── nome_do_projeto/
├── tests/
├── exemplos/
├── docs/
├── README.md
├── LICENSE
└── pyproject.toml
```

## Desenvolvimento

Descreva informações relevantes para desenvolver, modificar ou contribuir com o projeto.

## Autores

**Alunos**

* Caio Vinicius Guimarães de Lima (8ºsemestre)
* Isadora Daniel dos Santos (9º semestre)
* João Vitor Ballardin (9º semestre)

**Professores orientadores**

* Felipe Pinto da Motta Quevedo
* Felipe Schaedler de Almeida

## Referências

1. Slides disponibilizados pela professora Paula Manica na disciplina de Estruturas de Concreto Armado II.

2. Livro disponibilizado pelo professor João Ricardo Masuero na disciplina de Estruturas de Concreto Armado I.

3. Material didático sobre dimensionamento à flexão de elementos de concreto armado, referente ao Grupo I de concretos, com base na ABNT NBR 6118:2023.

4. Material didático sobre dimensionamento à flexão de elementos de concreto armado, referente ao Grupo II de concretos, com base na ABNT NBR 6118:2023.

5. Norma técnica ABNT NBR 6118:2026 — Projeto de estruturas de concreto — Procedimento.

## Licença

Este projeto está distribuído sob a licença MIT. Consulte o arquivo [`LICENSE`](LICENSE).

```



