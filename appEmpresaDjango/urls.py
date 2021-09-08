from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('departamento/<int:departamento_id>/', views.detail, name='detail'),
    path('departamento/<int:departamento_id>/empleado',views.empleados, name='empleados'),
    path('empleado/<int:empleado_id>', views.empledo, name='empleado'),
    path('habilidad/<int:habilidad_id>', views.habilidad, name='habilidad')
]