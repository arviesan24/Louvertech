from django import forms
from tinymce import TinyMCE
from .models import Gallery

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class UploadFileForm(forms.ModelForm):
    '''
    set the field attributes first before setting up the field's arrangement using the class Meta
    '''
    name = forms.CharField(label="Product Name", max_length=120)
    description = forms.CharField(widget=TinyMCEWidget(
            mce_attrs={'required': True, 'width': 'auto'}
        )
    )
    image_location = forms.ImageField(label="Upload Photo")

    class Meta:
        model = Gallery
        fields = ['name', 'description', 'image_location']