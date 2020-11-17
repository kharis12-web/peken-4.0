from django.forms import ModelForm
from . import models

class SalesForm(ModelForm):
    class Meta:
        model = models.Sale
        exclude=['owner']

    def __init__(self, *args, **kwargs):
        super(SalesForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['class'] = 'form-control'
        

class SaleDetail(ModelForm):
    class Meta:
        model = models.SaleDetail
        exclude=['owner','sale']
        
    def __init__(self, *args, **kwargs):
        super(SaleDetail, self).__init__(*args, **kwargs)
        self.fields['products'].widget.attrs['class'] = 'form-control'
        self.fields['qty'].widget.attrs['class'] = 'form-control'
        self.fields['desc'].widget.attrs['class'] = 'form-control'
        
