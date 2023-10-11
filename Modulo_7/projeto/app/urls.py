from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app.urls')), #app é o nome do diretório criado no comando startapp
    path('admin/', admin.site.urls),
]
