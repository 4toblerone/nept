from django import forms

class UploadForm(forms.Form):
	description = forms.CharField(widget=forms.Textarea)
	photo = forms.ImageField()