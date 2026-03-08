import requests
from django.http import JsonResponse
from django.conf import settings

API_KEY = '88687ba1669644d2b1562ab680e78bf6'

def live_score(request, match_id):
    try:
        response = requests.get(
            f'https://api.football-data.org/v4/matches/{match_id}',
            headers={'X-Auth-Token': API_KEY}
        )
        if response.status_code == 200:
            data = response.json()
            return JsonResponse({
                'home': data['score']['fullTime']['home'] or 0,
                'away': data['score']['fullTime']['away'] or 0,
                'homeTeam': data['homeTeam']['name'],
                'awayTeam': data['awayTeam']['name'],
                'status': data['status'],
                'minute': data.get('minute', 0),
                'period': data['status']  # or derive period from status/minute
            })
        else:
            return JsonResponse({'error': 'API error'}, status=500)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)