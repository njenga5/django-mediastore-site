import hashlib
from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.views.decorators.debug import sensitive_post_parameters
from django.conf import settings
from . import models, forms


def home_view(request):
    return render(request, "commonops/index.html", )


@sensitive_post_parameters()
def login(request,*args, **kwargs):
    form = forms.LoginForm()
    if request.method == 'GET':
        if 'user' in request.session:
            try:
                models.User.objects.get(email=request.session['user'])
                return redirect('dashboard:profile')
            except models.User.DoesNotExist:
                del request.session['user']
                return render(request, 'commonops/login.html', {'form': form})

    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            try:
                user = models.User.objects.get(email=form.cleaned_data.get('email'),
                                               password=hashlib.md5(form.cleaned_data.get('password').encode())
                                               .hexdigest())
            except models.User.DoesNotExist:
                return render(request, 'commonops/loginerror.html')
            try:
                del request.session['user']
            except KeyError:
                pass
            request.session['user'] = user.email
            return redirect('dashboard:profile')
    return render(request, 'commonops/login.html', {'form': form})


@sensitive_post_parameters('password', 'confirm_password', 'email')
def sign_up(request,*args, **kwargs):
    form = forms.SignUpForm()
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.date_of_birth = form.cleaned_data.get('date_of_birth')
            if form.cleaned_data.get('password') != form.cleaned_data.get('confirm_password'):
                return render(request, 'commonops/signuperror.html', {'error': 'Passwords do not match.'})
            user.password = hashlib.md5(form.cleaned_data.get('password').encode()).hexdigest()
            user.save()
            return redirect('commonops:auth')
        return render(request, 'commonops/signuperror.html', {'errors': form.errors})
    return render(request, 'commonops/signup.html', {'form': form})


def change_password(request,*args, **kwargs):
    form = forms.ChangePassForm()
    if request.method == "GET":
        return render(request, 'commonops/changepass.html', {'form': form})
    elif request.method == "POST":
        form = forms.ChangePassForm(request.POST)
        if form.is_valid():
            try:
                user = models.User.objects.get(email=form.cleaned_data.get('email'))
            except models.User.DoesNotExist:
                return render(request, 'commonops/changepasserror.html', {'form': form})
            subject = 'Account Password Change Request- Intranet.'
            message = f"""
                You have requested to change your account's password.
                Please click the link below to confirm.<br><br>
                <a href="http://localhost:8000/commonops/auth/"> Change Password.</a>
                <br><br><br>
                Don't recognize this action? Change your password immediately.
                Learn how to secure your account. <a href="http://localhost:8000/commonops/auth/">
                Learn more.</a>{'<br>'*5}
                <hr>
                This message was sent to {user.email} since you have an account with Intranet.
                If you are not {user.email}, please ignore this email.<br><br><br>
                    Yours,<br>
                    Intranet Team.
            """
            send_mail(subject, message, 'no-reply@intranet.com', [user.email], html_message=message)
            request.session['email'] = user.email
            return redirect('commonops:email-sent')
        return render(request, 'commonops/changepasserror.html', {'form': form, 'errors': form.errors})


def pricing_view(request,*args, **kwargs):
    return render(request, 'commonops/pricing.html', {})


def email_sent(request,*args, **kwargs):
    email = request.session.get('email')
    return render(request, 'commonops/emailsent.html', {'user': email})
