from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Departamento, Habilidad, Empleado

#devuelve el listado de empresas
def index(request):
    departamentos = get_list_or_404(Departamento.objects.order_by('nombre'))
    output = ", ".join([d.nombre for d in departamentos])
    return HttpResponse(output)

#devuelve los datos de un departamento
def detail(request, departamento_id):
    departamento = Departamento.objects.get(pk=departamento_id)
    #output = ", ".join([d.nombre for d in departamento])
    output = f"{departamento.id}, {departamento.nombre}, {departamento.telefono}"
    return HttpResponse(output)

#devuelve los empleados de un departamento
def empleados(request, departamento_id):
    departamento = get_object_or_404(Departamento.objects.get(pk=departamento_id))
    output = ", ".join([e.nombre for e in departamento.empleado_set.all()])
    return HttpResponse(output)

#devuelve los detalles de un empleado
def empledo(request, empleado_id):
    empleado = Empleado.objects.get(pk=empleado_id)
    #output = ", ".join([str(empleado.id), empleado.nombre, str(empleado.fecha_nacimiento), str(empleado.antiguedad), str(empleado.departamento), str([h.nombre for h in empleado.habilidades.all()])])
    datos_empleado = f"{empleado.id}, {empleado.nombre}, {empleado.fecha_nacimiento}, {empleado.antiguedad}, {empleado.departamento.nombre}"
    habilidades = ', '.join([h.nombre for h in empleado.habilidades.all()])
    output = f"{datos_empleado} // Habilidades: {habilidades}"
    return HttpResponse(output)

#devuelve los detalles de una habilidad

def habilidad(request,habilidad_id):
    print("ENTRE",habilidad_id)
    habilidad = Habilidad.objects.get(pk=habilidad_id)
    output = ", ".join([str(habilidad.id), habilidad.nombre, str([e.nombre for e in habilidad.empleado_set.all()])])
    return HttpResponse(output)