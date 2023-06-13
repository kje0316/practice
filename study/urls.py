from django.urls import path, include
from . import views

urlpatterns = [
    path('students', views.StudentView),
    path('students/<int:pk>', views.StudentDetailView),
    path('score', views.score_view),
    path('score/<int:pk>', views.Score_DetailView), 
    path('students/<int:pk>/score', views.StudentScoreView),
]
