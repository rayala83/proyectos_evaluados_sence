from django.urls import path
from .views import transfer_view, login_view, logout_view, dashboard_view, transactions_view, deposit_view

urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('transfer/', transfer_view, name='transfer'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('transactions/', transactions_view, name='transactions'),
    path('deposit/', deposit_view, name='deposit'),
]