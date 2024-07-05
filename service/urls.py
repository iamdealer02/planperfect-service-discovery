from django.urls import path
from .views import register_service, discover_service, deregister_service

urlpatterns = [
    path('register/', register_service, name='register_service'),
    path('discover/<str:name>/', discover_service, name='discover_service'),
    path('deregister/<str:name>/', deregister_service, name='deregister_service'),
]
