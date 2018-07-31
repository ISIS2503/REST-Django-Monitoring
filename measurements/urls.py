from django.urls import path

from . import views

urlpatterns = [
    path('', views.MeasurementListCreate.as_view()),
    path('<int:pk>/', views.MeasurementDetail.as_view()),
]