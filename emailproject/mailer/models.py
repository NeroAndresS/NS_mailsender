from django.db import models
from django.contrib.auth.models import User
from django_summernote.fields import SummernoteTextFormField
# Create your models here.

class MailingList(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    users = models.ManyToManyField(User, related_name='mailing_lists')

    def __str__(self):
        return self.name

class Email(models.Model):
    subject = models.CharField(max_length=200)
    body = SummernoteTextFormField()
    mailing_list = models.ForeignKey(MailingList, on_delete=models.CASCADE, related_name='emails')
    sent_at = models.DateTimeField(null=True, blank=True)