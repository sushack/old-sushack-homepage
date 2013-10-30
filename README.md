The Django application for http://sushack.co.uk


Instructions for installation:

    mkvirtualenv sushack
    workon sushack
    pip install -r requirements.txt
    psql#: create database sushack;
    python manage.py syncdb
    python manage.py migrate

Now let's start the dev server:

    DEBUG=True python manage.py runserver

or

    DEBUG=True ./manage.py runserver
