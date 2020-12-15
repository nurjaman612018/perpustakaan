from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse
from perpusapp.models import Buku , Kelas
from perpusapp.forms import FormBuku, FormKelas
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from perpusapp.resource import BukuResource

def export_xls(request):
    buku = BukuResource()
    dataset = buku.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=buku.xls'
    return response




def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User sudah berhasil dibuat")
            return redirect('signup')
        else:
            messages.error(request,"Terjadi Kesalahan")
            return redirect('signup')
    else:
        form = UserCreationForm()
        konteks = {
            'form': form,
        }
    return render(request,'daftar.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def buku(request):
    #jika ingin di filter dengan nama pada kelas 
    #books = Buku.objects.filter(kelas_id__nama='X MIPA 1')
    
    books = Buku.objects.all()#jika ingin menampilkan data hanya 3[:3]
    
    konteks = {
        'books' : books,        
    }
  
    return render(request,'buku.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def tambah_buku(request):
    if request.POST:
        
        form = FormBuku(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormBuku()
            pesan = "Data berhasil di simpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request,'tambah-buku.html', konteks)
    else:
        form = FormBuku()

        konteks = {
            'form': form,
        }   
    return render(request, 'tambah-buku.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def ubah_buku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = 'ubah-buku.html'
    if request.POST:
        form = FormBuku(request.POST, request.FILES, instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil di perbaharui")
            return redirect('ubah_buku', id_buku=id_buku)
    else: 
        form = FormBuku(instance=buku)
        konteks = {
            'form':form,
            'buku':buku,
        }
    return render(request, template, konteks)

@login_required(login_url=settings.LOGIN_URL)
def hapus_buku(request, id_buku):
    buku = Buku.objects.filter(id=id_buku)
    buku.delete()
    messages.success(request, "Data berhasil dihapus !")
    return redirect('buku')

#---------------------------------------------------------------#
# --------------------- KELAS ----------------------------------#
#---------------------------------------------------------------#

def kelas(request):
    kelas = Kelas.objects.all()

    konteks = {
        'kls' : kelas,
    }
    return render(request, 'kelas.html', konteks)

def tambah_kelas(request):
    if request.POST:
        
        form = FormKelas(request.POST)
        if form.is_valid():
            form.save()
            form = FormKelas()
            pesan = "Data berhasil di simpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request,'tambah-kelas.html', konteks)
    else:
        form = FormKelas()

        konteks = {
            'form': form,
        }   
    return render(request, 'tambah-kelas.html', konteks)

def ubah_kelas(request, id_kelas):
    kelas = Kelas.objects.get(id=id_kelas)
    template = 'ubah-kelas.html'
    if request.POST:
        form = FormKelas(request.POST, instance=kelas)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil di perbaharui")
            return redirect('ubah_kelas', id_kelas=id_kelas)
    else: 
        form = FormKelas(instance=kelas)
        konteks = {
            'form':form,
            'kelas':kelas,
        }
    return render(request, template, konteks)

def hapus_kelas(request, id_kelas):
    kelas = Kelas.objects.filter(id=id_kelas)
    kelas.delete()
    messages.success(request, "Data berhasil di hapus !")
    return redirect('kelas')

