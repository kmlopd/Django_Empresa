from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)

from .models import Empleado
from .forms import EmpleadoForm

# Create your views here.

class InicioView(TemplateView):
    template_name = 'home/inicio.html'

class ListAllEmpleados(ListView):
    template_name = 'empleado/list_all.html'
    paginate_by = 2
    ordering = 'nom'
    model = Empleado

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de Empleados'

        print(context)

        return context

class ListByDptoEmpleado(ListView):
    template_name = 'empleado/list_by_dpto.html'

    def get_queryset(self):
        x = self.kwargs['valDpto']
        rtaLista  = Empleado.objects.filter(
            dpto__nom = x
        )
        return rtaLista
    

    
class ListaEmpleadoByKword(ListView):
    template_name = 'empleado/find_empleado.html'
    context_object_name = 'rtaEmpleados'

    def get_queryset(self):
        x = self.request.GET.get("valNom",'')
        rtaLista = Empleado.objects.filter(
            nom = x
        )
        return rtaLista
    



class ListaDeCursosEmpleado(ListView):
    template_name = 'empleado/list_by_cursos.html'
    context_object_name = 'rtaCursos'

    def get_queryset(self):
        
        x = self.request.GET.get("valId")
        if x:
            try:
                x = int(x)
                empleado = Empleado.objects.get(id=x)
                return empleado.curso.all()
            except (ValueError, Empleado.DoesNotExist): 
                return Empleado.objects.none()
        else:
            return Empleado.objects.none()
        

class DetalleEmpleado(DetailView):
    model = Empleado
    templatename= 'empleado/detail_empleado.html'

class CrearEmpleado(CreateView):
    model = Empleado
    template_name= 'empleado/add_empleado.html'
    form_class = EmpleadoForm
    fields= ['nom', 'tipo', 'dpto']
    fields = ('__all__')
    success_url = reverse_lazy('controlEmpleado_app:registro_correcto')

    def form_valid(self, form):
        empleado = form.save()
        empleado.nom = empleado.nom.upper()
        empleado.save
        return super(CrearEmpleado, self).form_valid(form)

class SuccesView(TemplateView):
    template_name = 'empleado/succes.html'


class UpdateEmpleado(UpdateView):
    model = Empleado
    template_name = 'empleado/update_empleado.html'
    fields = ('__all__')
    success_url = reverse_lazy('controlEmpleado_app:registro_correcto')

class DeleteEmpleado(DeleteView):
    model = Empleado
    template_name = 'empleado/delete_empleado.html'
    success_url = reverse_lazy('controlEmpleado_app:registro_correcto')
