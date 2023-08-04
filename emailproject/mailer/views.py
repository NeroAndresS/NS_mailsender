from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MailingList, Email
from .forms import EmailForm,MailingListForm

# Create your views here.

@login_required
def mailing_list_view(request):
    user = request.user
    mailing_lists = user.mailing_lists.all()
    return render(request, 'mailing_list.html', {'mailing_lists': mailing_lists})

@login_required
def mailing_list_view(request):
    if request.method == 'POST':
        form = MailingListForm(request.POST)
        if form.is_valid():
            mailing_list = form.save(commit=False)
            mailing_list.save()
            mailing_list.users.add(request.user)
    else:
        form = MailingListForm()

    user = request.user
    mailing_lists = user.mailing_lists.all()
    return render(request, 'mailing_list.html', {'mailing_lists': mailing_lists, 'form': form})
@login_required
def send_email_view(request, mailing_list_id):
    mailing_list = MailingList.objects.get(pk=mailing_list_id)
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            email = Email.objects.create(subject=subject, body=body, mailing_list=mailing_list)

            # Sending the email using Django's email framework
            send_mail(subject, body, 'your_gmail_username@gmail.com', [mailing_list.email], fail_silently=False)
            return redirect('mailing_list')
    else:
        form = EmailForm()

    return render(request, 'send_email.html', {'form': form, 'mailing_list': mailing_list})