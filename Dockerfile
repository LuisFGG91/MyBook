FROM python:3.9

#env/bin/python manage.py makemigrations usuarios

#ENV FLASK_APP run.py

COPY manage.py gunicorn-cfg.py requirements.txt .env db.sqlite3 ./
COPY apps apps
COPY core core

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#RUN python manage.py makemigrations usuarios
#RUN python manage.py migrate

EXPOSE 5006
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "core.wsgi"]

