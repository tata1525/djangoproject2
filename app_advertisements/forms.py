from django.forms import ModelForm
from .models import Advertisement
from django import forms


class AdvertisementForm(ModelForm):
    class Meta:
        model=Advertisement
        fields=['title','description','price','auction','image']
        widgets={
            'description': forms.Textarea(attrs={'class':'form-control form-control-lg'}),
            'price': forms.NumberInput(attrs={'class':'form-control form-control-lg'}),
            'auction': forms.CheckboxInput,
            'image': forms.FileInput(attrs={'class':'form-control form-control-lg'})
        }
