Work on this for now, and then we'll migrate the code to a public repo on SusHack organization later


Instructions for installation:

    mkvirtualenv sushack
    workon sushack
    pip install -r requirements.txt

Now let's start the dev server:

    DEBUG=1 AWS_ACCESS_KEY_ID=id AWS_SECRET_ACCESS_KEY=secret python manage.py runserver
