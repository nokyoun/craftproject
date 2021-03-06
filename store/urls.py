from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('store', views.store, name="store"),
    path('store2/', views.store2, name="store2"),
    path('store3/', views.store3, name="store3"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('updateItem/', views.updateItem, name="updateItem"),
    path("register/", views.registerPage, name="register"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logoutUser, name="logout"),
    path('manage/', views.manage, name="manage"),
    path('custPage/', views.custPage, name="custPage"),
    path('viewBtn/', views.viewBtn, name="viewBtn"),

]


