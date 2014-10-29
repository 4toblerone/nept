from django import forms
from models import Post

class UploadForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea)
    photo = forms.ImageField()
    municipality = forms.ChoiceField(widget=forms.Select,
                                     choices=((x,x) for x in Post.MUNICIPALITY),label="Opstina")