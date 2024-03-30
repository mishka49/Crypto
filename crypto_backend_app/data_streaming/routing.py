from django.urls import path
from .consumers import DashBoardConsumer

websocket_urlpatterns = [
    path('ws/<str:dashboard_slug>/', DashBoardConsumer.as_asgi()),

]