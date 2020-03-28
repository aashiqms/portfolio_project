from django import forms
from django.core import validators
from portfolio_app.models import User

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
           
        
   #  name = forms.CharField()
    # email = forms.EmailField()
   # verify_email = forms.EmailField(label='enter your email again')
  #  text = forms.CharField(widget=forms.Textarea)

