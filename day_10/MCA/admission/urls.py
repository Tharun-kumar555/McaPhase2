from django.urls import path 
from.import views

urlpatterns = [
 
    # path("Ac/",views.Ac,name='Ac'),
    # path("Ad/",views.Ad,name='Ad'),
    # path("At/",views.At,name='At'),
    path('admission/', views.index, name='app1_index'),
    # path('', views.index1, name='app2_index'),
    # path("",views.Home,name='Home'),
]
