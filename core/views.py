from django.shortcuts import render
from core.models import models


def index(request):

    return render(request, 'index.html')