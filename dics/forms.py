from django import forms

class SearchForm(forms.Form):
    search_query = forms.CharField(label='Search for a word', max_length=100, required=False)