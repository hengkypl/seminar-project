from django.shortcuts import render, redirect, get_object_or_404
from .models import Peserta
from .forms import PesertaForm

# Create your views here.

def pesertahome(request):
    zpesertas = Peserta.objects
    return render(request, 'peserta/peserta.html', {'zpeserta':zpesertas})


def register(request):
    post = Peserta()
    if request.method == 'POST':
        peserta_form = PesertaForm(data=request.POST)
        new_peserta = peserta_form.save(commit=False)
        new_peserta.post = post
        new_peserta.save()
        return redirect('pesertahome')
    else:
        return render(request, 'peserta/register.html',
                     {'peserta_form': PesertaForm})
