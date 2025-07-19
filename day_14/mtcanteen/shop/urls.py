from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<str:cat>/', views.category_view, name='category'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]
