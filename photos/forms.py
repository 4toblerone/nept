from django import forms
from models import Post

class UploadForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea,)
    photo = forms.ImageField()
    #change to text field with auto-complete
    city_part = forms.ChoiceField(widget=forms.Select,
                                     choices=((x,x) for x in Post.MUNICIPALITY),label="Opstina")