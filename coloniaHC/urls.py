
from django.contrib import admin
from django.urls import path
from coloniaHC.views import nuevo_usuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nuevousuario/', nuevo_usuario)
]
