from django import forms

from .models import Gallery

class UploadFileForm(forms.ModelForm):
    '''
    set the field attributes first before setting up the field's arrangement using the class Meta
    '''
    name = forms.CharField(label="Product Name", max_length=120)
    description = forms.CharField(label="Details", widget=forms.Textarea(attrs={'cols': 10, 'rows': 5}), max_length=2000)
    image_location = forms.ImageField(label="Upload Photo")

    class Meta:
        model = Gallery
        fields = ['name', 'description', 'image_location']