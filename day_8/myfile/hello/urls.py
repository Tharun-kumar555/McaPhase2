from django.urls import path
from . import views
urlpatterns=[path('home/',views.home,name='home'),
             path('yes/',views.yes,name='yes'),
             path('page/',views.page,name='page'),
             ]
# urlpatterns=[path('yes/',views.yes,name='yes'