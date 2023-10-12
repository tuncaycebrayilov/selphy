from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['price_review', 'value_review', 'quality_review', 'nickname', 'review']
        widgets = {
            'nickname': forms.TextInput(attrs={'class': 'form-group'}),
            'review' : forms.Textarea(attrs={'class': 'form-group'}),
        }