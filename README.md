## 📋 Descrição

A API tem como objetivo receber uma base de dados com informações de compras de produtos e a partir disso indicar produtos recomendados.
Essa recomendação foi feita a partir de um algoritmo de recomendação previamente escolhido.


Como não temos informações prévias dos usuários ou do comportamento deles, você deverá escolher e implementar um algoritmo ou heurística para a recomendação de produtos. Justifique a escolha deste algoritmo ou heurística na documentação.


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
git clone git@github.com:anniasebold/flask-openai.git
```

## Configuração das variáveis de ambiente

Criação do arquivo .env

```bash
touch .env
```
Dentro terão duas variáveis de ambiente:

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
docker-compose --build
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