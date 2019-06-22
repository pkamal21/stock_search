from django import forms

from .models import Query

class PostForm(forms.ModelForm):

    class Meta:
        model = Query
        fields = ('query',)