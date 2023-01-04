from django.urls import path
from main import views

urlpatterns = [
    path('home/', views.homepage, name='home'),
    path('login/', views.loginpage, name='login'),
    path('register/', views.registerpage, name='register'),
    path('logout/', views.logoutpage, name='logout'),
]