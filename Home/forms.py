from django import forms
class Contact(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone = forms.IntegerField()
    content = forms.CharField(widget=forms.Textarea)