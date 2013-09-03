SHELL := /bin/bash

help:
    @echo "usage:"
    @echo "    make deploy -- deploy to Heroku"
    @echo "    make static -- build static files to s3"

deploy:
    git push heroku master

static:
    STATICFILES_STORAGE='incuna_storages.backends.S3StaticStorage' python manage.py collectstatic -i *.sass --noinput
