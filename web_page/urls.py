from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from RuthMunoz import views

urlpatterns = [
    path("", views.home, name= "home"),
    path("RuthMunoz/<name>", views.hello_there, name="hello_there"),
]

urlpatterns += staticfiles_urlpatterns()

