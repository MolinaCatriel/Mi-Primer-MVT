from django.urls import path
from familiares.views import mostrar_familiares

urlpatterns = [
    path('', mostrar_familiares)
]