from django import forms
from blog.models import Comment
from .models import NewsletterEmail
# from captcha.fields import CaptchaField



class CommentForm(forms.ModelForm):

    class Meta:
        model=Comment
        fields=['subject','message']
        
    
class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterEmail
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
                'required': True,
            }),
        }