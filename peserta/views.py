from django.shortcuts import render
from .models import Peserta


# Create your views here.

def pesertahome(request):
    return render(request, 'peserta/peserta.html')


def register(request):
    if request.method == 'POST':
        peserta = Peserta()
        peserta.nama=request.POST['']
        peserta.save()

    else:
        return render(request, 'register.html')
