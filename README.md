# Quiz Interativo

Este projeto oferece um quiz simples utilizando FastAPI no backend e uma página HTML/JavaScript na pasta `static` para o frontend. As perguntas do quiz são extraídas de um arquivo PDF e armazenadas em um banco SQLite.

## Preparação do ambiente

1. Crie um ambiente virtual e instale as dependências:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Gerando as questões a partir de um PDF

1. Coloque o seu PDF com as perguntas na raiz do repositório (onde já existe `questions.pdf`).
2. Abra `main.py` e altere a variável `pdf_path` para o nome do seu arquivo.
3. Execute o script para extrair as questões e gravá-las em `quiz_questions.db`:

```bash
python main.py
```

## Executando o backend

Para iniciar a API e servir o frontend, execute:

```bash
uvicorn backend.api:app --reload
```

Abra `http://localhost:8000` no navegador para acessar o quiz.

## Implantação

O arquivo `render.yaml` mostra um exemplo de configuração para a plataforma Render. O comando utilizado é:

```bash
uvicorn backend.api:app --host 0.0.0.0 --port 10000
```

Adapte conforme a plataforma de hospedagem escolhida.
