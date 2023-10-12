from django import forms
from .models import Comment

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['commenter_name', 'comment_body', 'email', 'phone']
        widgets = {
            'commenter_name': forms.TextInput(attrs={'class': 'form-control'}),
            'commenter_body' : forms.Textarea(attrs={'class': 'form-comtrol'}),
            'email' : forms.TextInput(attrs={'class': 'form-control'}),
            'phone' :  forms.TextInput(attrs={'class': 'form-control'})
        }