from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
import sys
print("MAIN URLS LOADING", file=sys.stderr)
def ping(request):
    return JsonResponse({"ping": "pong"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ping/', ping),
    path('api/', include('scores.urls')),
]