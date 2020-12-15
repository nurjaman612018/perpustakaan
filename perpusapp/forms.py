from django.forms import ModelForm
from django import forms
from perpusapp.models import Buku , Kelas

class FormBuku(ModelForm):
    class Meta:
        model = Buku
        fields = '__all__'

        widgets = {
            'judul' : forms.TextInput({'class':'form-control'}),
            'penulis' : forms.TextInput({'class':'form-control'}),
            'penerbit' : forms.TextInput({'class':'form-control'}),
            'jumlah' : forms.NumberInput({'class':'form-control'}),
            'kelas_id' : forms.Select({'class':'form-control'}),
            'kelompok_id' : forms.Select({'class':'form-control'}),
            
        }

class FormKelas(ModelForm):
    class Meta:
        model = Kelas
        fields = '__all__'
    
        widgets = {
            'nama': forms.TextInput({'class':'form-control'}),
            'keterangan': forms.TextInput({'class':'form-control'}),
        }
