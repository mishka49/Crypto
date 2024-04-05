from django.urls import path
from .views import main, dashboard

app_name = 'stats'

urlpatterns = [
    path('<str:room_name>/', dashboard, name='dashboard'),
]
