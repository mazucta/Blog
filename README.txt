python -m pip install --upgrade pip
pip install django
django-admin startproject blog_project
cd blog_project
python manage.py startapp blog
python manage.py migrate
python manage.py runserver

активация виртуального окружения 
venv\scripts\activate


при изминении структуры таблиц базы 
python manage.py makemigrations 
python manage.py migrate

регистрация админа 
python manage.py createsuperuser

Работа с изоброжениями 
pip install pillow