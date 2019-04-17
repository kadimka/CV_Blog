from django import forms
from .models import Post, Comment, Task


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'image')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('task_name', 'task_progress', 'user')
