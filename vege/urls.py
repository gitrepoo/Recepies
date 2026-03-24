from django.urls import path
from . import views
from .views import ReceipeExportAPIView


app_name = 'vege'
urlpatterns = [
    path('receipe/', views.receipe, name='receipe'),
    path('receipe/export/', ReceipeExportAPIView.as_view(), name="receipe_export"),

] 

