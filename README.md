# Versiones
python --version
python -m django --version

pip install -r requirements.txt


# RUN SERVER POR DEFECTO, CAMBIO DE PUERTO Y CAMBIO DE SERVIDOR
python manage.py runserver
python manage.py runserver 8080
python manage.py runserver 0.0.0.0:8080

# CREACION DE TABLAS EN LA BASE DE DATOS
python manage.py makemigrations
python manage.py migrate

# INICIANDO PROYECTO
django-admin startproject app

# PANEL DE ADMINISTRACION
# CREAR SUPER USUARIO
python manage.py createsuperuser
user: own
password: own
email: okwalluis@gmail.com

# OTROS MODULOS
python startapp personas
python startapp prestamos
python startapp cuotas_prestamo
python startapp website
...

# INICIALIZANDO GIT PARA CONTROL DE VERSION
git config --global user.name "Luis Olmedo"
git config --global user.email "okwalluis@gmail.com"
git config --global push.default matching
git config --global alias.co checkout
git init

git add .
git commit -am 'Commit inicial'

## Nos conectamos a Github creamos un repositorio y luego, en el  apartado de ...or push an existing repository from the command line - ejecutamos esto!
git remote add origin https://github.com/okwalluis/urutau.git
git branch -M main
git push -u origin main

## Subir actualizaciones
git add .
git commit -am "<comentario>"
git push

## Ver ramas
git remote -v
git remote show origin
