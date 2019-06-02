from django.contrib import admin
from .models import Peserta


#admin.site.register(Peserta)


class PesertaAdmin(admin.ModelAdmin):
    def tglindo(self, obj):
        return obj.tgllahir.strftime("%d-%m-%Y")

    tglindo.short_description = "Tgl Lahir"

    list_display = ('nama', 'tglindo', 'jemaat', 'wilayah', 'hp', 'tshirt', 'catatan')
    list_filter = ['wilayah']
    search_fields = ['nama', 'hp']

admin.site.register(Peserta, PesertaAdmin)

admin.site.site_header='Application Dashboard'
admin.site.site_title = "Dashboard - Seminar Pasutri";
