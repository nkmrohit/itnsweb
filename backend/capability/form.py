from django import forms
from django.core.exceptions import ValidationError
from capability import models
from capability.models import capability

class capabilityForm(forms.ModelForm):
    name         = forms.CharField(label='Name',max_length=100)
    description  = forms.Textarea()
    image = forms.FileField(label='Image')
    logo = forms.FileField(label='Logo')
    #created = forms.DateTimeField()
    #updated = forms.DateTimeField()
    
    def __init__(self, *args, **kwargs):
        super(capabilityForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        """Meta definition for MODELNAMEform."""
        model = capability
        fields = ('id','name','description','image','logo')

