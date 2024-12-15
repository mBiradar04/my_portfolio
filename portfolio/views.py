# Create your views here.

from django.shortcuts import render
from .models import Project, Skill


def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    return render(request, 'home.html',
                  {'projects': projects, 'skills': skills})