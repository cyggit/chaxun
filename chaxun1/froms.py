__author__ = 'cyg'

from django.forms import  ModelForm
from chaxun1.models import yonghu


class UserLogin(ModelForm):
    class Meta:
        model=yonghu
        fields=('name','password')


