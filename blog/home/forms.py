from django.forms import ModelForm
from home.models import Post,Comment

# Create the form class.
class PostForm(ModelForm):
     class Meta:
        model = Post
        fields = ['title', 'text']
        
        
class CommentForm(ModelForm):
     class Meta:
        model = Comment
        fields = ['text']