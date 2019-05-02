from django.contrib import admin
from .models import Peserta


#admin.site.register(Peserta)

class PesertaAdmin(admin.ModelAdmin):
    list_display = ('nama', 'tgllahir', 'jemaat', 'wilayah', 'hp', 'tshirt')
    list_filter = ['wilayah']
    search_fields = ['nama', 'hp']

admin.site.register(Peserta, PesertaAdmin)
