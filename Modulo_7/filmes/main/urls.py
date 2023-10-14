from django.urls import path
from .import views

main = 'main'

urlpatterns = [
    path("", views.homepage, name='homepage'),   
]