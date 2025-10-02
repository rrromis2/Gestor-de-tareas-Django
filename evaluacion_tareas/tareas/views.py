from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Tarea

class TareaListView(ListView):
    model = Tarea
    template_name = "tareas/tarea_list.html"

class TareaDetailView(DetailView):
    model = Tarea
    template_name = "tareas/tarea_detail.html"

class TareaCreateView(CreateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'prioridad', 'vigente', 'fecha_limite']
    template_name = "tareas/tarea_form.html"
    success_url = reverse_lazy('tarea_list')

class TareaUpdateView(UpdateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'prioridad', 'vigente', 'fecha_limite']
    template_name = "tareas/tarea_form.html"
    success_url = reverse_lazy('tarea_list')

class TareaDeleteView(DeleteView):
    model = Tarea
    template_name = "tareas/tarea_confirm_delete.html"
    success_url = reverse_lazy('tarea_list')