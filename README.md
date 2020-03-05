# Work at Olist

[![Build Status](https://travis-ci.org/mayronceccon/work-at-olist-library.svg?branch=master)](https://travis-ci.org/mayronceccon/work-at-olist-library)

# Installation
```bash
git clone git@github.com:mayronceccon/work-at-olist-library.git

cd work-at-olist-library

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

cp .env.example .env

docker-compose up --build

python manage.py migrate
```

# Test
```
python manage.py test
```

## Coverage Report
```
coverage run manage.py test && coverage html
```

# Environment
|   |   |
|---|---|
Computer||
S.O|Fedora 31|
Editor|VSCode|
Django Version|3.0.3|
Python Version||
Django Rest Framework Version|3.11.0|
Docker Compose Version||

# Documentation

[https://library-work-at-olist.herokuapp.com/](https://library-work-at-olist.herokuapp.com/)
