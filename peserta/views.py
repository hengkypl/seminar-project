from django.shortcuts import render, redirect, get_object_or_404
from .models import Peserta

# Create your views here.

def pesertahome(request):
    zpesertas = Peserta.objects
    return render(request, 'peserta/peserta.html', {'zpeserta':zpesertas})


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
        return redirect('pesertahome')

    else:
        return render(request, 'peserta/register.html')
