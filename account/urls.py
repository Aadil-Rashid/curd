from django.urls import path
from . import views
from django.contrib.auth import views as authViews
# from account import urls

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name='register'),
    path('login/', authViews.LoginView.as_view(template_name="account/login.html"), name="login"),
    path('logout/', authViews.LogoutView.as_view(template_name="account/logout.html"), name="logout"),
    path('profile/', views.profileView, name="profile"),
    path('about/', views.aboutView, name="about"),
]
