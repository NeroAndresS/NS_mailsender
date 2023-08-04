from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import MailingList

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=200)
    body = forms.CharField(widget=SummernoteWidget())
class MailingListForm(forms.ModelForm):
    class Meta:
        model = MailingList
        fields = ['name', 'email']