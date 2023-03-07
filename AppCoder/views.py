from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso


def courses(request):
    return render(request, "index.html")