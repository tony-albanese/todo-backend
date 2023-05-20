# To-Do List Backend

# Setup
* Download or clone the repository.
* Make sure `pipenv` is installed.
```
pip install pipenv
```

* Then install the required packages.
  ```
  pipenv install -r requirements.txt
  ```

> Make sure your virtual environent is activated.

>Installed djanco with command: python -m pip install Django

>django-admin startproject todo
> settings.py: add newly installed app(line 40 todo,)
> create env.py
>import os if exists in settings.py

>Migrate: python manage.py migrate

> create prifiles app: python manage.py startapp profiles
> settings.py: add profiles to installed apps

>signals to create a profile everytime a user is created
>migrate: python manage.py makemigrations
python manage.py migrate

>create superuser: python manage.py createsuperuser
> username: aiman
> aimanpass12