import sys
print("Loading scores/views.py", file=sys.stderr)
from django.http import JsonResponse

def live_score(request, match_id):
    return JsonResponse({"match_id": match_id, "message": "Live score endpoint hit"})

def test_api(request):
    return JsonResponse({'message': 'API is working'})