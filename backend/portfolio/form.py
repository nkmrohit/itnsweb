from django import forms
from django.core.exceptions import ValidationError
from portfolio import models
from portfolio.models import portfolios

class portfolioForm(forms.ModelForm):
    name         = forms.CharField(label='Name',max_length=100)
    description  = forms.Textarea()
    image = forms.FileField(label='Image')
    #created = forms.DateTimeField()
    #updated = forms.DateTimeField()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        """Meta definition for MODELNAMEform."""
        model = portfolios
        fields = ('id','name','description','image')

