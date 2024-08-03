# trades/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.trade_list, name='trade_list'),
    path('trade/<int:pk>/', views.trade_detail, name='trade_detail'),
    path('trade/new/', views.add_trade, name='add_trade'),

    path('trade/<int:pk>/edit/', views.edit_trade, name='edit_trade'),
    path('trade/<int:pk>/delete/', views.delete_trade, name='delete_trade'),
]
