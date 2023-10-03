from django.urls import path
from . import views

urlpatterns = [
    path("", views.auth_home, name=""),
    path("login/", views.auth_login, name=""),    
    path("signup/", views.auth_signup, name=""),    

]
