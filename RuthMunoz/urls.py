from django.urls import path
from RuthMunoz import views

urlpatterns = [
    path("", views.home, name="home"),
    path("RuthMunoz/<name>", views.hello_there, name="hello_there")
]