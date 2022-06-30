from django import forms
from .models import PostModel, Comment


# The Post form
class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))

    class Meta:
        model = PostModel
        fields = ('title', 'content')


# Edit post form
class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('title', 'content')


# comment form
class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Add comment here...'}))

    class Meta:
        model = Comment
        fields = ('content',)
