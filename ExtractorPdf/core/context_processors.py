# core/context_processors.py
from django.urls import reverse

def menu_items(request):
    return {
        'menu_items': [
            {'name': 'Lista de Setores', 'url': reverse('setor-list')},
            {'name': 'Outro Item', 'url': reverse('setor-create')},
            # Adicione mais itens conforme necessário
        ]
    }