WWW_DREW=/var/www/drew

BASE_LOCATION=$(shell cd ../. && pwd)
WEB_LOCATION=$(BASE_LOCATION)/web

LOGS_LOCATION=$(BASE_LOCATION)/logs

VIRTUALENV_LOCATION=$(BASE_LOCATION)/virtualenv

PYTHON_BIN=$(VIRTUALENV_LOCATION)/bin/python3.5

PIP=$(VIRTUALENV_LOCATION)/bin/pip3

DREW_SITE_AV=/etc/nginx/sites-available/drew
DREW_SITE_EN=/etc/nginx/sites-enabled/drew

DREW_APP_AV=/etc/uwsgi/apps-available/drew.ini
DREW_APP_EN=/etc/uwsgi/apps-enabled/drew.ini

install_python:
	apt-get install python3
	sudo apt-get install python3-pip python3-dev build-essential

install_dependencies:
	apt-get install virtualenv libjpeg-dev libfreetype6 libfreetype6-dev zlib1g-dev

virtualenv:
	virtualenv -p /usr/bin/python3.5 $(BASE_LOCATION)/virtualenv
	$(PIP) install -r $(BASE_LOCATION)/deploy/requirements.txt
	$(PIP) install uwsgi
	chown -R $(USER):$(USER) $(BASE_LOCATION)/virtualenv

logs:
	[ -d $(LOGS_LOCATION) ] || mkdir $(LOGS_LOCATION)
	touch $(LOGS_LOCATION)/debug.log
	touch $(LOGS_LOCATION)/normal.log
	touch $(LOGS_LOCATION)/summary.log

dirs:
	[ -d $(WEB_LOCATION)/uploads/product_files ] || mkdir -p $(WEB_LOCATION)/uploads/product_files

migrate:
	cd $(WEB_LOCATION); $(PYTHON_BIN) manage.py migrate

collectstatic:
	cd $(WEB_LOCATION); $(PYTHON_BIN) manage.py collectstatic --noinput

permissions:
	chown -R $(USER):$(USER) ../*

www:
	[ -L $(WWW_DREW) ] || ln -s $(BASE_LOCATION) $(WWW_DREW)

nginx:
	[ -L $(DREW_SITE_AV) ] || ln -s $(BASE_LOCATION)/deploy/etc/nginx/sites-available/drew $(DREW_SITE_AV)
	[ -L $(DREW_SITE_EN) ] || ln -s $(DREW_SITE_AV) $(DREW_SITE_EN)

uwsgi:
	[ -L $(DREW_APP_AV) ] || ln -s $(BASE_LOCATION)/deploy/etc/uwsgi/apps-available/drew.ini $(DREW_APP_AV)
	[ -L $(DREW_APP_EN) ] || ln -s $(DREW_APP_AV) $(DREW_APP_EN)

deploy: install_python install_dependencies virtualenv logs dirs migrate collectstatic permissions www uwsgi nginx

cleanpyc:
	find -type f -name "*.pyc" | xargs rm

cleanlogs:
	rm -rf $(LOGS_LOCATION)

cleanvirtualenv:
	rm -rf $(BASE_LOCATION)/virtualenv

easy_clean: cleanpyc cleanlogs logs
full_clean:	cleanpyc cleanlogs cleanvirtualenv logs virtualenv

remove_links:
	[ ! -L $(DREW_SITE_EN) ] || rm $(DREW_SITE_EN)
	[ ! -L $(DREW_SITE_AV) ] || rm $(DREW_SITE_AV)
	[ ! -L $(DREW_APP_EN) ] || rm $(DREW_APP_EN)
	[ ! -L $(DREW_APP_AV) ] || rm $(DREW_APP_AV)
	[ ! -L $(WWW_DREW) ] || rm $(WWW_DREW)