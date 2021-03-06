from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Departamento, Habilidad, Empleado


#devuelve el listado de empresas
# def index(request):
#     departamentos = get_list_or_404(Departamento.objects.order_by('nombre'))
#     #output = ", ".join([d.nombre for d in departamentos])
#     #return HttpResponse(output)
#     context = {
#         'lista_departamentos': departamentos
#     }
#     return render(request,'index.html',context)
class DepartamentoListView(ListView):
    model = Departamento
    template_name = 'index.html'
    queryset = Departamento.objects.order_by('nombre')      #En la vista se llamada como departamento_list por convencion lo relaciona.

    def get_context_data(self, **kwargs):
        context = super(DepartamentoListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listado de departamentos'
        return context


#devuelve los datos de un departamento
# def detail(request, departamento_id):
#     departamento = Departamento.objects.get(pk=departamento_id)
#     #output = ", ".join([d.nombre for d in departamento])
#     #output = f"{departamento.id}, {departamento.nombre}, {departamento.telefono}"
#     #return HttpResponse(output)
#     context = {
#         'departamento': departamento
#     }
#     return render(request,'detail.html',context)
class DepartamentoDetailView(DetailView):
    model = Departamento
    template_name = 'detail.html'


#devuelve los empleados de un departamento
def empleados(request, departamento_id):
    departamento = Departamento.objects.get(pk=departamento_id)
    #output = ", ".join([e.nombre for e in departamento.empleado_set.all()])
    #return HttpResponse(output)
    context = {
        'departamento':departamento
    }
    return render(request,'empleados.html',context)

#devuelve los detalles de un empleado
# def empleado(request, empleado_id):
#     empleado = Empleado.objects.get(pk=empleado_id)
#     #output = ", ".join([str(empleado.id), empleado.nombre, str(empleado.fecha_nacimiento), str(empleado.antiguedad), str(empleado.departamento), str([h.nombre for h in empleado.habilidades.all()])])
#
#     #datos_empleado = f"{empleado.id}, {empleado.nombre}, {empleado.fecha_nacimiento}, {empleado.antiguedad}, {empleado.departamento.nombre}"
#     #habilidades = ', '.join([h.nombre for h in empleado.habilidades.all()])
#     #output = f"{datos_empleado} // Habilidades: {habilidades}"
#     #return HttpResponse(output)
#     context = {
#         'empleado': empleado,
#         'habilidades': empleado.habilidades.all()
#     }
#     return render(request,'empleado.html',context)

class EmpleadoDetailView(DetailView):

    model = Empleado
    template_name = 'empleado.html'     #La convencion dicta que debe ser empleado_detail.html

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView,self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles del empleado'
        return context

#devuelve los detalles de una habilidad
def habilidad(request,habilidad_id):
    print("ENTRE",habilidad_id)
    habilidad = Habilidad.objects.get(pk=habilidad_id)
    #output = ", ".join([str(habilidad.id), habilidad.nombre, str([e.nombre for e in habilidad.empleado_set.all()])])
    #return HttpResponse(output)
    context = {
        'habilidad' : habilidad,
        'empleados' : habilidad.empleado_set.all()
    }
    return render(request,'habilidad.html',context)

