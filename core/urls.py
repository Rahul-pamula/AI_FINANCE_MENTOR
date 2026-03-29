from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('chat/', views.chat_view, name='chat'),
    path('api/score/', views.calculate_score, name='api_score'),
    path('api/sip/', views.suggest_sip, name='api_sip'),
    path('api/chat/', views.ai_chat, name='api_chat'),
]
