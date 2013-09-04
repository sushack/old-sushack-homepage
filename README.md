Work on this for now, and then we'll migrate the code to a public repo on SusHack organization later


Instructions for installation:

    mkvirtualenv sushack
    workon sushack
    pip install -r requirements.txt
    psql#: create database sushack;
    python manage.py syncdb

Now let's start the dev server:

    python manage.py runserver

or

    ./manage.py runserver
