from django.urls import path
from . import views  # Importamos las vistas de la aplicación productos

app_name = 'solicitudes'  # Definimos un espacio de nombres para las URLs
urlpatterns = [
    path('', views.lista_solicitudes, name='lista'),
    path('nuevo/', views.create_solicitud, name='nuevo'),
    path('editar/<int:pk>/', views.edit_solicitud, name='editar'),
    path('eliminar/<int:pk>/', views.delete_solicitud, name='eliminar'),
]
