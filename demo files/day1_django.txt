Day 1 Django tutorial tailored for absolute beginners. This tutorial covers the essential setup and helps you build your first Django project step-by-step.
________________________________________
🌐 What is Django?
Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It's built by experienced developers and handles much of the hassle of web development.
________________________________________
✅ Day 1 Goals
•	Install Django
•	Create your first Django project
•	Run the development server
•	Create a simple app
•	Create your first view and URL
________________________________________
🛠️ Step 1: Install Django
Make sure Python is installed:

python --version
If not, install it from python.org.
Create and activate a virtual environment:

python -m venv env
source env/bin/activate   # On Windows use: env\Scripts\activate
Install Django:

pip install django
Verify Django installation:

django-admin --version
________________________________________
📁 Step 2: Create Your First Project

django-admin startproject mysite
cd mysite
Folder structure:

mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
________________________________________
▶️ Step 3: Run the Development Server

python manage.py runserver
Visit: http://127.0.0.1:8000/
You should see the Django welcome page.
ctrl+c
________________________________________
🧱 Step 4: Create Your First App
Django projects are made of multiple apps. Let’s create one called hello.

python manage.py startapp hello
You’ll now see a new folder hello/ with these files:

hello/
    admin.py
    apps.py
    models.py
    tests.py
    views.py
    ...
________________________________________
🔗 Step 5: Add the App to Settings
Open mysite/settings.py and add 'hello', to INSTALLED_APPS:

INSTALLED_APPS = [
    ...
    'hello',
]
________________________________________
📄 Step 6: Create a Simple View
Open hello/views.py and add:

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")
________________________________________
🛣️ Step 7: Create URL Configuration
In hello/, create a file called urls.py:

from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),

]

Now connect this to the main project’s URL configuration.
Open mysite/urls.py and modify:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('hello.urls')),
]
________________________________________
🧪 Step 8: Test the App
Run the server again (if it’s not already running):

python manage.py runserver
Visit: http://127.0.0.1:8000/hello/home/
You should see: Hello, Django!
________________________________________
🎯 Recap for Day 1
You've learned:
•	How to set up Django
•	How to create a project and an app
•	How views and URLs work

