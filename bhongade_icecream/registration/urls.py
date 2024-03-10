from django.urls import path
from registration import views




urlpatterns=[
    path('', views.homepage, name='home'),
    path('save/home/', views.homepage, name='home'),
    path('list/home/', views.homepage, name='home'),
    path('edit/home/', views.homepage, name='home'),
    path('delete/home/', views.homepage, name='home'),
    path('list/edit/home/', views.homepage, name='home'),
    path('login/', views.LoginPage, name='login'),
    path('signup/', views.SignUpPage, name='signup'),
    path('logout/', views.LogoutPage, name='logout'),
    

]