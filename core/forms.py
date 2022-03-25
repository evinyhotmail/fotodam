from csv import field_size_limit
from django import forms
from django.forms import ModelForm
from core.models import *

class ImageForm(ModelForm):
    title = forms.CharField(
    label='*Titulo.',
    required=True,
    max_length=80,
    widget=forms.TextInput(attrs={'class': 'form-control', }))

    description = forms.CharField(
    label='*Descripción.',
    required=True,
    widget=forms.Textarea(attrs={'class': 'form-control',
                                    'cols': 30,
                                    'rows': 4,
                                    'maxlength': '120',
                                    }))
   
    categories = forms.MultipleChoiceField(
        label='*Categorías actuales.',
        required=True,
        widget=forms.CheckboxSelectMultiple(
        attrs={'class':'category-check'}
        ),
        choices=[
            (c.pk, c.description) for c in ImageCategory.objects.all().order_by('description')],
           
    )

    image = forms.FileField (
    label='*Imagen.',
    help_text="Formatos aceptados: .jpg, .png .pdf", 
    required=True,
    widget=forms.FileInput(
        {'class':'custom-file-input'}
        
    )
    )

    class Meta:
        model = ImageBank
        fields = [
            'title',
            'description',
            'categories',
            'image',

        ]

