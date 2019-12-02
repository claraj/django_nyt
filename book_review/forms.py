from django import forms 

class BookSearchForm(forms.Form):
    author = forms.CharField(label='Author', max_length=100)

