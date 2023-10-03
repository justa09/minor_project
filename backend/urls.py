from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.home),
    path("auth/", include("AppAuth.urls"), name=""),
    path('admin/', admin.site.urls),
]
