from django.contrib import admin
from perpusapp.models import Buku , Kelompok , Kelas

# Register your models here.
class BukuAdmin(admin.ModelAdmin):
    list_display = ['judul','kelompok_id','kelas_id','jumlah']
    search_fields = ['judul','penulis','penerbit']
    list_filter = ('kelompok_id','kelas_id')
    list_per_page = 2

admin.site.register(Buku, BukuAdmin)
admin.site.register(Kelompok)
admin.site.register(Kelas)
