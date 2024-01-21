# Django web admin

Django web admin interface for managing sellers, products and quotas.
This app contains all database models and must be used to update any.

## How to start

Activate virtural environment and install dependencies:

```sh
python3 venv venv
./venv/Scripts/activate
pip install -r requirements.txt
```

from web folder run migrations, create superuser and run server:

```sh
python manage.py makemigrations
python manage.py migrate managers 
python manage.py migrate {app name}
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8080
```
