from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('update_item/<int:pk>/', views.update_item, name='update_item'),
    path('delete_item/<int:pk>/', views.delete_item, name='delete_item'),
    path('update_status/<int:pk>/', views.update_status, name='update_status'),
]