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

python manage.py migrate
```

# Test
```bash
python manage.py test
```

## Coverage Report
```bash
coverage run manage.py test && coverage html
```

# Environment
|   |   |
|---|---|
S.O|Fedora 31|
Editor|VSCode 1.42.1|
Django Version|3.0.3|
Python Version|3.7.6|
Django Rest Framework Version|3.11.0|

# Documentation

[https://library-work-at-olist.herokuapp.com/](https://library-work-at-olist.herokuapp.com/)

## Authors Import
```bash
python manage.py import_authors filename.csv
```
