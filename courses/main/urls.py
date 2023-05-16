from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import *

# urlpatterns = [
#     path('', views.products, name='products'),
#     path('register/', views.register, name='register'),
#     path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),
# ]
urlpatterns = [
    path('', views.products, name='products'),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", user_logout, name="logout"),
    path("profile/", profile, name="profile"),
    path("basket/", basket_view, name="basket"),
    path("create_receipt/", create_receipt, name="create_receipt"),
    path('add_to_basket/<int:pk>', add_to_basket, name='add_to_basket'),
    path('remove_from_basket/<int:pk>', remove_from_basket, name='remove_from_basket'),
    path('remove_from_basket_products/<int:pk>', remove_from_basket_products, name='remove_from_basket_products'),
    path('create_product/', create_product, name='create_product'),
    path('update_product/<int:pk>', UpdateProduct.as_view(), name='update_product'),
    path('delete_product/<int:pk>', delete_product, name='delete_product'),
    path('update_user/<int:user_id>/', update_user, name='update_user'),
    path('product_page/<int:pk>/', product_page, name='product_page'),
]
