Work on this for now, and then we'll migrate the code to a public repo on SusHack organization later


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
