from django.urls import path
from AppCoder.views import courses
urlpatterns = [
    path('cursos/', courses),
]
