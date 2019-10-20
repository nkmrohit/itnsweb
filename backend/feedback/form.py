from django import forms
from django.core.exceptions import ValidationError
from feedback import models
from feedback.models import feedbacks

class feedbackForm(forms.ModelForm):
    name         = forms.CharField(label='Name',max_length=100)
    link         = forms.CharField(label='Link',max_length=100)
    description  = forms.Textarea()
    image = forms.FileField(label='Image')
    #created = forms.DateTimeField()
    #updated = forms.DateTimeField()
    
    def __init__(self, *args, **kwargs):
        super(feedbackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        """Meta definition for MODELNAMEform."""
        model = feedbacks
        fields = ('id','name','link','description','image')

