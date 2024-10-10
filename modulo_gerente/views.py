from django.views.generic import TemplateView, View

# Vista para el Dashboard principal
class DashboardView(TemplateView):
    template_name = 'modulo_gerente/dashboard.html'

# Vista para Metas
class MetasView(TemplateView):
    template_name = 'modulo_gerente/metas.html'

# Vista para Descanso
class DescansosView(TemplateView):
    template_name = 'modulo_gerente/descansos.html'

# Vista para Datos Agentes
class DatosAgentesView(TemplateView):
    template_name = 'modulo_gerente/datos_agentes.html'

def perfil_gerente_view(request):
    # Aquí puedes obtener información específica del gerente
    return render(request, 'modulo_gerente/perfil.html')

from django.shortcuts import render
import requests

from django.shortcuts import render

def gerente_dashboards(request):
    return render(request, 'modulo_gerente/dashboard.html')
