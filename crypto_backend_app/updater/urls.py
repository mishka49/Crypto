from django.urls import path

from updater.views import UpdateView

urlpatterns = [
    path('update/', UpdateView.as_view()),
]