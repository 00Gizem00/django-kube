from django.shortcuts import render
from .models import TestModel

# Create your views here.

def index(request):

    test_models = TestModel.objects.all()

    return render(request, 'index.html', {'test_models': test_models})