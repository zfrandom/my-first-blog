from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
	class Meta: #which model should be used to create this form
		model = Post
		fields = ('title','text',) #which field should end up in our form

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('author', 'text',)
