from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [
    path('home/',views.home,name='home'),
    path('product_list/', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('signup/', views.signup, name='signup'),
    path('remove-from-cart/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('', auth_views.LoginView.as_view(template_name='login.html',next_page='product_list'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('update-cart/<int:pk>/', views.update_cart_quantity, name='update_cart_quantity'),
    path('place-order/',views.place_order,name='place_order'),
    path('order-history/',views.order_history,name='order_history'),
    path('download-bill-pdf/', views.download_bill_pdf, name='download_bill_pdf'),
]