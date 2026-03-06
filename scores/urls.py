from django.urls import path
from . import views


urlpatterns = [
        path('test/', views.test_api, name='test_api'),
    path('live/<int:match_id>/', views.live_score, name='live_score'),
]
