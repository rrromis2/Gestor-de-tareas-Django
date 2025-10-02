from django.urls import path
from . import views

urlpatterns = [
    path('tarea/', views.TareaListView.as_view(), name='tarea_list'),   # lista
    path('tarea/<int:pk>/', views.TareaDetailView.as_view(), name='tarea_detail'),
    path('tarea/nueva/', views.TareaCreateView.as_view(), name='tarea_create'),
    path('tarea/<int:pk>/editar/', views.TareaUpdateView.as_view(), name='tarea_update'),
    path('tarea/<int:pk>/eliminar/', views.TareaDeleteView.as_view(), name='tarea_delete'),
]
