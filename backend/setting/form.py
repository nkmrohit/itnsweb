from django import forms
from django.core.exceptions import ValidationError
from setting import models
from setting.models import settings
from ckeditor.widgets import CKEditorWidget

class settingForm(forms.ModelForm):
    #name         = forms.CharField(label='Name',max_length=100)
    logo            = forms.FileField(label='Logo')
    tagline         = forms.CharField(label='Tagline',max_length=50)
    favicon         = forms.FileField(label='Favicon')
    name            = forms.CharField(label='Name')
    email           = forms.EmailField(label='Email')
    phone           = forms.IntegerField(label='Phone')
    facebook        = forms.CharField(label='Facebook')
    twitter         = forms.CharField(label='Twitter')
    linkedin        = forms.CharField(label='LinkedIn')
    seo             = forms.Textarea()
    meta            = forms.Textarea()
    footerContent   = forms.Textarea()

    #created = forms.DateTimeField()
    #updated = forms.DateTimeField()
    
    def __init__(self, *args, **kwargs):
        super(settingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        """Meta definition for MODELNAMEform."""
        model = settings
        fields = ('id','name','logo','tagline','favicon','email','phone','facebook','twitter','linkedin','seo','meta','footerContent')

