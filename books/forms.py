from django import forms
from .models import Books 


class BookForm(forms.ModelForm):

    class Meta:
        model = Books
        fields = ('book_title', 'author', 'pages', 'book_cover', 'storyline')