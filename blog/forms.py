from django import forms
from blog.models import Images


class ImagesForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter title',
            }),
            'display_image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Select banner image',
            }),
        }