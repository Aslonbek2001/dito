from django.shortcuts import render
from .models import Foto

def index(request):
    context = {
        'fotos': Foto.objects.all()
    }
    return render(request, 'index.html', context)



