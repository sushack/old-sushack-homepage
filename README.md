The Django application for the old (November 2013) http://sushack.co.uk/

We're using a Jekyll-based approach now, you can find the source at http://github.com/omgmog/sushack.co.uk/


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
