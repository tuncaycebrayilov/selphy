from django import forms
from django.forms import widgets
from .models import LeaveMessage, Subscriber


class SubscriberForm(forms.ModelForm):
        class Meta:
                model = Subscriber
                fields = ('email',)
                widgets = {
                'email': widgets.EmailInput(attrs={'class': 'input-text required-entry validate-email', 
                'palceholder': 'Enter your email address'} ),
                }

        def clean_email(self):
                email = self.cleaned_data.get('email')
                if Subscriber.objects.filter(email=email).exists():
                        raise forms.ValidationError("Email already in use")
                return email


class LeaveMessageForm(forms.ModelForm):

        class Meta:
                model = LeaveMessage
                fields = '__all__'