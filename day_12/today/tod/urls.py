from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('green/',views.displaygreen,name="displaygreen"),
    path('display/',views.display,name="display"),
    path('table/',views.testing,name="testing"),
]
