from django.urls import path
from . import views

urlpatterns = [
    path('', views.juego1, name='Juego1'),
    path('registrar', views.registrar_participante, name='Registrar'),
    path('resultados', views.resultados, name='Resultados'),
    path('participantes', views.participantes, name='Participantes'),
    path('comprar', views.comprar, name='Comprar'),
]