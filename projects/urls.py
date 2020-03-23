from django.urls import path

from . import views

urlpatterns = [
    path('', views.allprojects, name='allprojects'),
    path('<int:project_id>/', views.project_detail, name='project_detail'),
]
