SHELL := /bin/bash
CHDIR_SHELL := $(SHELL)

# Pix4d - exercise inventory of drones and cameras

ENV = env
MANAGE = ./manage.py
REQUIREMENT = requirements/local.txt
PORT = 8000

all:
	##### automatically run the project with all requirements
	make -j4 server

install:
	virtualenv $(ENV) -p python2 --prompt="(`basename \`pwd\``)"
	pip install -r $(REQUIREMENT)

server:
	$(MANAGE) runserver 127.0.0.1:$(PORT)

heroku:
	#### Create and deploy Heroku instance
ifdef LOGIN
	heroku login
endif
ifdef CREATE
	heroku create pix4dexercise
endif
	heroku config:set --app pix4dexercise DJANGO_SETTINGS_MODULE=settings.heroku
	git push heroku master
	heroku run python manage.py migrate
	heroku open
