# analytics_views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from .models import VentasUnitarias
from django.db.models import Sum
from .utils import validate_dates_and_agents

@api_view(['GET'])
def ventas_totales_view(request):
    """
    Endpoint API para calcular las ventas totales filtradas por fecha y agentes.
    """
    params = validate_dates_and_agents(request, default_start_date=datetime.today().replace(day=1))
    if isinstance(params, Response):
        return params  # Retornar error si las fechas o agentes son inválidos

    start_date = params['start_date']
    end_date = params['end_date']
    agentes = params['agentes']

    # Filtrar las ventas según las fechas y agentes
    ventas_query = VentasUnitarias.objects.filter(fecha__range=[start_date, end_date])
    if agentes:
        ventas_query = ventas_query.filter(id_usuario__in=agentes)

    # Calcular el total de ventas
    total_ventas = ventas_query.aggregate(total=Sum('total_venta'))['total'] or 0

    return Response({'total_ventas': total_ventas})
