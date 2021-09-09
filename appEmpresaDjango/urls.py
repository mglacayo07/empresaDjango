from django.urls import path
from . import views

urlpatterns = [
    path('',views.DepartamentoListView.as_view(), name='index'),
    path('departamento/<int:pk>/', views.DepartamentoDetailView.as_view(), name='detail'),
    path('departamento/<int:departamento_id>/empleados',views.empleados, name='empleados'),
    path('empleado/<int:pk>', views.EmpleadoDetailView.as_view(), name='empleado'),
    path('habilidad/<int:habilidad_id>', views.habilidad, name='habilidad')
]