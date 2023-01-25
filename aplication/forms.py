from django.forms import ModelForm
from .models import *
from allauth.account.forms import SignupForm

#ACCOUNT_SIGNUP_FORM_CLASS = 'aplication.forms.MyProfileSignupForm'


class AnunciarForm(ModelForm):
     class Meta:
         model = Post
         fields = ['title', 'cat','description','amount', 'price','premium',]
#adicionar todo o resto depois,imagens e etc

class VerifiedForm(ModelForm):
    class Meta:
        model = Verified
        fields = ['telephone','rg','cpf','cep','birthdate','address','city','state','country',]

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body',]

