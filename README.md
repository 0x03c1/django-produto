# Projeto Store

### Configuração do ambiente de desenvolvimento

- Para a criação do ambiente virtual e ativação do mesmo

```bash
python -m venv .venv
```

- Ativição do ambiente virtual no Windows
```bash
.venv\Scripts\activate # Windows users
```

- Ativição do ambiente virtual no Linux
```bash
.venv/bin/activate # Unix users
```

Agora vamos instalar a biblioteca do Django em nosso ambiente virtual

```bash
pip install django
```

- Criar o arquivo requirements.txt com as bibliotecas necessárias para o funcionamento do projeto
```bash
pip freeze > requirements.txt
```
