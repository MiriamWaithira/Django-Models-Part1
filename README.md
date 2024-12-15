# Django-Models-Part1
This is the first part of learning the Django Models


In this project, we create a system where one can poll.

Setting up the Project:
Create the virtual environment named pollSystem using the command: 'virtualenv pollSystem'.
To activate it, use the command: 'source Scripts/activate'.
Install the django project using: 'pip install django'.
Create the django project inside the pollSystem using: 'django-admin startproject mysite'.
Navigate into the django project:'cd mysite'.
Test if the site is running: 'python manage.py runserver'.
Create the django app using: 'django-admin startapp myapp'.
By now, we have the django app inside the django project, proceed to configure the settings, etc.
Go to the settings and register your app: '->pollSystem-> mysite-> mysite-> settings.py' in the installed apps add 'myapp'.
Create your views in the views.py in myapp.
Create 'urls.py' file in 'mysite' and create your own urls and url patterns. This is because you could have different apps inside the same django project.

Creating Databases:
To apply migrations, use: 'python manage.py migrate'. The django application has created all those tables and configured the migrations.

Creating the User Interface for the Database:
Go to 'models.py' in 'myapp' to define the database. Create the classes here.
Make the migrations for the models/changes made in 'models.py' in 'myapp' using: 'python manage.py makemigrations myapp'.
To see the setup for the tables, use: 'python manage.py sqlmigrate myapp 0001' to return their SQL.

Setting up the Database:
Set up the log in credentials to access the database. Use the command: 'python manage.py createsuperuser'. Follow the given prompts given.
To log in run 'python manage.py runserver' then use the url 'http://127.0.0.1:8000/admin/'. Use the credentials used to create the super user to login.

It’s important to add __str__() methods to your models:
    i. for your own convenience when dealing with the interactive prompt
    ii. because objects’ representations are used throughout Django’s automatically-generated admin.
Go to 'admin.py' in 'myapp' and register the models there.
Add more views e.g. detail, results and vote in the 'views.py' in 'myapp'.
Add urlpatterns in the 'urls.py' file in the 'myapp'.