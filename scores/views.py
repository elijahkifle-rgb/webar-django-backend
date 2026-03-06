from django.shortcuts import render

# Create your views here.
import sys
print("Loading scores/views.py", file=sys.stderr)
from django.http import JsonResponse

def test_api(request):
    return JsonResponse({'message': 'API is working'})