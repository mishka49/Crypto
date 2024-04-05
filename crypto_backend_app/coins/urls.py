from django.urls import path

from coins import views

urlpatterns = [
    path('', views.coins, name='coins'),
    path('filter_by_name/', views.coins_filtered_by_name),
    path('filter_by_rank/', views.coins_filtered_by_rank),
    path('filter_by_price/', views.coins_filtered_by_price),
    path('filter_by_percent_change/<segment>', views.coins_filtered_by_percent_change)
]