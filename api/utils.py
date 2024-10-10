# utils.py
from datetime import datetime
from rest_framework.response import Response

def parse_date(date_str, date_format='%Y-%m-%d'):
    """
    Convierte una cadena de texto a un objeto datetime.
    """
    try:
        return datetime.strptime(date_str, date_format)
    except (ValueError, TypeError):
        return None

def parse_agent_list(agents_str):
    """
    Convierte una cadena de texto con IDs de agentes separados por comas en una lista de enteros.
    """
    try:
        if agents_str:
            return [int(a) for a in agents_str.split(',')]
        return []
    except ValueError:
        return None

def validate_dates_and_agents(request, default_start_date=None):
    """
    Valida y convierte los parámetros de fecha y agentes desde la solicitud.
    """
    start_date_str = request.query_params.get('start_date')
    end_date_str = request.query_params.get('end_date')
    agentes_str = request.query_params.get('agentes')

    # Validar y convertir las fechas
    start_date = parse_date(start_date_str) or default_start_date
    end_date = parse_date(end_date_str) or datetime.today()

    if not start_date or not end_date:
        return Response({'error': 'Formato de fecha inválido. Use YYYY-MM-DD.'}, status=400)

    # Validar y convertir la lista de agentes
    agentes = parse_agent_list(agentes_str)
    if agentes is None:
        return Response({'error': 'El ID de agentes debe ser un número.'}, status=400)

    return {'start_date': start_date, 'end_date': end_date, 'agentes': agentes}
