from django.urls import path
from . import views

# app_name = 'transactions'
urlpatterns = [
    path('upload-csv/', views.upload_csv, name='upload_csv'),
    path('empty-database/',views.empty_database, name='empty_database'),
    path('transactions/upload', views.upload_transaction),
    path('transactions/', views.get_transactions),
    path('transactions/<int:pk>/', views.update_transaction),
    path('transactions/<int:pk>/delete/', views.delete_transaction),
    # Other URL patterns...
]