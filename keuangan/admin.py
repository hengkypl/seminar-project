from django.contrib import admin
from .models import Keuangan

#admin.site.register(Peserta)

class KeuanganAdmin(admin.ModelAdmin):

    list_display = ('tanggal', 'kategori', 'keterangan', 'masuk', 'keluar')
    list_filter = ['kategori', 'tanggal']
    search_fields = ['tanggal']

admin.site.register(Keuangan, KeuanganAdmin)
