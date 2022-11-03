from django import forms
from .models import Post
from django.contrib.auth.decorators import login_required

class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = [
           'title',
           'text',
           'categoryType',
           'author_post'
       ]
