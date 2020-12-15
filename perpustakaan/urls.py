
from django.contrib import admin
from django.urls import path
from perpusapp.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buku/', buku , name='buku'),
    path('tambah-buku/', tambah_buku, name='tambah_buku'),
    path('buku/ubah/<int:id_buku>', ubah_buku, name='ubah_buku'),
    path('buku/hapus/<int:id_buku>', hapus_buku, name='hapus_buku'),

    path('kelas/',kelas, name='kelas'),
    path('kelas/hapus/<int:id_kelas>',hapus_kelas, name='hapus_kelas'),
    path('tambah-kelas/', tambah_kelas, name='tambah_kelas'),
    path('kelas/ubahkelas/<int:id_kelas>', ubah_kelas, name='ubah_kelas'),
    path('masuk/', LoginView.as_view(), name='masuk'),
    path("keluar/", LogoutView.as_view(next_page='masuk'), name="keluar"),
    path('signup/', signup, name='signup'),  
    path('export/xls', export_xls, name='export_xls'), 

] 

#ditambahkan agar gambar masuk ke dalam tabel
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
