from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('transfer/', views.transfer_view, name='transfer'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('transactions/', views.transactions_view, name='transactions'),
    path('deposit/', views.deposit_view, name='deposit'),
    path('contacts/', views.contact_list, name='contacts'),
    path('contacts/create/', views.contact_create, name='contact_create'),
    path('contacts/<int:id>/', views.contact_detail, name='contact_detail'),
    path('contacts/<int:id>/edit/', views.contact_update, name='contact_edit'),
    path('contacts/<int:id>/delete/', views.contact_delete, name='contact_delete'),
]