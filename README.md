# Event-planer


## Student Name: Mohammad Shahin

## End Points
- Event/ :
    http://127.0.0.1:8000/Event/
    to get the list of top 10 events

- weather/ : 
    http://127.0.0.1:8000/weather/?id=33BmzXrL7kKcj9XqXS
    to get the weather at that loction 

- flights/:
    http://127.0.0.1:8000/flights/?id=37BkvbWqPsy2tRNHM5&airport_code=KATL
    mention the nearby airport and the flights

## Table of Contents
* **[Installation](#installation)**
  * [Pip](#pip)
  
* 
----



## 🚀 Features

- Django 4.2 & Python 3.11
- Install via [Pip](https://pypi.org/project/pip/) or [Docker](https://www.docker.com/)
- User log in/out, sign up, password reset via [django-allauth](https://github.com/pennersr/django-allauth)
- install  django rest framework via: pip install djangorestframework
- used psql as data base
- added how to restrict access to portions of your APIs data
----



## 📖 Installation
Django can be installed via Pip 

```
$ git clone git@github.com:Mohammad-Shahin23/Event-planer.git
$ cd Event-planer
```

### Pip

```
$ python -m venv .venv

# Windows
$ Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
$ .venv\Scripts\Activate.ps1


(.venv) $ pip install -r requirements.txt
(.venv) $ python manage.py migrate
(.venv) $ python manage.py createsuperuser
(.venv) $ python manage.py runserver
# Load the site at http://127.0.0.1:8000
```

