from django.shortcuts import render,redirect
from .models import Peserta


# Create your views here.

def pesertahome(request):
    return render(request, 'peserta/peserta.html')


def register(request):
    if request.method == 'POST':
        peserta = Peserta()
        peserta.nama = request.POST['nama']
        peserta.tgllahir = request.POST['tgllahir']
        peserta.hp = request.POST['hp']
        peserta.jemaat = request.POST['jemaat']
        peserta.wilayah = request.POST['wilayah']
        peserta.tshirt = request.POST['tshirt']
        peserta.catatan = request.POST['catatan']
        peserta.foto = request.FILES['foto']
        peserta.save()
        return redirect('home')

    else:
        return render(request, 'peserta/register.html')
