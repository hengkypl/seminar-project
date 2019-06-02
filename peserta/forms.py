from django import forms
from .models import Peserta
from django.forms.widgets import SelectDateWidget

class PesertaForm(forms.ModelForm):
    class Meta:
        model = Peserta
        labels  = {
            'nama':'Nama Lengkap',
            'tgllahir':'Tanggal Lahir',
            'hp':'Nomor HP',
            'jemaat':'Jemaat',
            'wilayah':'Majelis Daerah',
            'tshirt':'Ukuran T-Shirt'
            }
        fields = ('nama', 'tgllahir', 'hp', 'jemaat', 'wilayah', 'tshirt', 'catatan', 'foto')
        widgets = {
            'tgllahir': forms.SelectDateWidget(years=range(1940, 1999), attrs={'style': 'display: inline-block; width: 15%;'}),
        }
