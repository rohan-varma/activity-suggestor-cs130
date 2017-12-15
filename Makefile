default: install

install:
		pip3 install -r requirements.txt

server:
		cd mysite && python3 manage.py runserver

tests:
		cd mysite && python3 manage.py test