from django.urls import path
from . import views

urlpatterns = [
    path('live/<int:match_id>/', views.live_score, name='live_score'),
]