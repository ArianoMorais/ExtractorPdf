from django.urls import path
from .views import (
    SetorListView, SetorCreateView, SetorUpdateView, SetorDeleteView, HomeView,
    InteressadoListView, InteressadoCreateView, InteressadoUpdateView, InteressadoDeleteView
)

urlpatterns = [
    # URLs para Setor
    path('', HomeView.as_view(), name='home'),
    path('setores/', SetorListView.as_view(), name='setor-list'),
    path('setores/novo/', SetorCreateView.as_view(), name='setor-create'),
    path('setores/<int:pk>/editar/', SetorUpdateView.as_view(), name='setor-update'),
    path('setores/<int:pk>/deletar/', SetorDeleteView.as_view(), name='setor-delete'),

    # URLs para Interessado
    path('interessados/', InteressadoListView.as_view(), name='interessado-list'),
    path('interessados/novo/', InteressadoCreateView.as_view(), name='interessado-create'),
    path('interessados/<int:pk>/editar/', InteressadoUpdateView.as_view(), name='interessado-update'),
    path('interessados/<int:pk>/deletar/', InteressadoDeleteView.as_view(), name='interessado-delete'),
]