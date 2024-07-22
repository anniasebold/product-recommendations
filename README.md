## 📋 Descrição

A API tem como objetivo receber uma base de dados com informações de compras de produtos e a partir disso indicar produtos recomendados.

## 🔎 Escolha do algoritmo

O algoritmo de recomendação foi desenvolvido para identificar e recomendar os produtos mais populares e de melhor desempenho de vendas com base em dados históricos. 

Inicialmente não temos informações prévias dos usuários ou do comportamento deles, portanto, a recomendação é baseada exclusivamente em dados de vendas anteriores.

### Como o algoritmo funciona:

  1. Criação de Colunas:
      - `total_sales`: Calcula o total de vendas por produto em todo o período analisado.
      - `store_frequency`: Conta a frequência do produto em cada loja.
      - `sales_per_store`: Soma das vendas diárias para cada combinação de produto e loja.

  2. Agrupamento e Seleção:
      - Os produtos são agrupados por `product_id` e `store_id`, e são calculados os valores de `total_sales`, `store_frequency` e `sales_per_store` para cada grupo.
      - Para cada produto, a loja com a maior frequência e o maior número total de vendas diárias é selecionada. Isso garante que estamos considerando tanto a frequência de compra na loja quanto o volume de vendas da loja.

  3. Seleção dos Produtos:
      - Após identificar a melhor loja para cada produto, os produtos são classificados com base no total de vendas. Os 5 produtos com os maiores totais de vendas são selecionados como recomendações.

- Assim, o algoritmo recomenda os 5 produtos mais vendidos, levando em conta a frequência do produto nas lojas e o total de vendas por loja. Isso gera uma recomendação mais assertiva onde são recomendados produtos que têm um alto número de vendas e que tem uma popularidade maior.

## 💻 Tecnologias utilizadas

- **Flask**: Framework para a criação de APIs web.
- **pytest**: Ferramenta de testes unitários para garantir a qualidade do código.
- **pylint**: Ferramenta de análise de código estático para padronização e boas práticas.
- **Docker**: Plataforma de contêineres para criar, distribuir e executar aplicações.
- **Docker Compose**: Ferramenta para orquestração de aplicações multi-contêiner.

Essas foram as tecnologias utilizadas para construção da aplicação de forma que ela fosse escalável, bem testada e fácil de configurar.

# 💾 Como utilizar

## Clonando o repositório

```bash
git clone git@github.com:anniasebold/product-recommendations.git
```

## Configuração das variáveis de ambiente

Criação do arquivo .env

```bash
touch .env
```
Dentro terá uma variável de ambiente:

```bash
FILE_PATH=xpto_sales_products_mar_may_2024.csv
```

Insira o nome do arquivo e se o arquivo não estiver na mesma pasta do projeto o seu caminho.

## Configuração do ambiente

### Pré requisitos

- docker
- docker-compose

Para realizar a configuração do ambiente é necessário o docker e o docker-compose instalados previamente.

Na primeira vez executando é necessário rodar o build

```bash
docker-compose up --build
```

Após isso suba a aplicação
```bash
docker-compose up web
```

A partir da primeira execução o --build não é mais necessário.

## Utilização da aplicação

A aplicação estará disponível: http://127.0.0.1:5000

Exemplo de uso:

```bash
curl --request GET \
  --url http://127.0.0.1:5000/product-recommendations/:user_id \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/8.5.0'
```

Substitua __user_id__ pelo user_id respectivo (a verificação não foi implementada então seria fictício).

## Testes unitários

Execução dos testes unitários:
```bash
docker-compose run tests pytest
```

Execução dos teste unitários detalhados:
```bash
docker-compose run tests pytest -s -v
```

## Configuração do ambiente virtual (opcional)

### Pré requisitos

- Python 3.9
- pip

Se você não quiser utilizar o Docker e quiser construir o ambiente na sua máquina é necessário o Python e o pip instalados previamente.

Criação do venv

```bash
python3 -m venv .venv
```

Ativação do ambiente virtual

```bash
source .venv/bin/activate
```

Instalação das dependências

```bash
pip install -r requirements.txt
```

Execução da aplicação

```bash
python3 run.py
```
Execução dos testes unitários
```bash
pytest
```

Execução dos testes unitários detalhados:
```bash
pytest -s -v
```