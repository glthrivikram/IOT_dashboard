from django.forms import ModelForm
from dash import models 
class fieldForm(ModelForm):
    class Meta:
        model = models.feild
        fields = '__all__'

class dataForm(ModelForm):
    class Meta:
        model = models.data
        fields = '__all__'
    