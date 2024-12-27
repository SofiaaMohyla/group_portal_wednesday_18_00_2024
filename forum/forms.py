from django import forms
from .models import Forum
from .models import Comment

class ForumFormCreate(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['title']

class ForumFormEdit(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['title']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']