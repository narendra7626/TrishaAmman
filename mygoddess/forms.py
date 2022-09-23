from django import forms
from mygoddess.models import *
from django.contrib.admin.widgets import AdminDateWidget

RELIGION_CHOICES = [
    ('trishaism', 'Trishaism'),
]

gen = [('male','Male'),('female','Female')]

class DevoteesForm(forms.ModelForm):
    religion = forms.ChoiceField(choices=RELIGION_CHOICES)
    class Meta:
        model = Devotees
        fields = ['name', 'religion','picture','story']

class DateInput(forms.DateInput):
    input_type = 'date'

class SevaForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = Seva
        fields = ['devotee', 'name', 'date']

class ProfileForm(forms.ModelForm):
    gender =forms.ChoiceField(choices=gen,widget=forms.RadioSelect())
    class Meta:
        model = Profile
        fields = ['image','gender','experience']
    
class TrishaSlaveForm(forms.ModelForm):
    class Meta:
        model = TrishaSlave
        fields = ['image','description']
   
  

