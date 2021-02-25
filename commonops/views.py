from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, reverse
from django.views.decorators.debug import sensitive_post_parameters
from django.conf import settings
from . import models, forms


def home_view(request):
    return render(request, "commonops/index.html", )


@sensitive_post_parameters()
def login_view(request):
    form = forms.LoginForm()
    if request.method == 'GET':

        if request.user.is_authenticated:
            try:
                models.CustomUser.objects.get(email=request.user.email)
                return redirect('dashboard:profile')
            except models.CustomUser.DoesNotExist:
                return render(request, 'commonops/login.html', {'form': form})

    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard:profile')
            else:
                return render(request, 'commonops/loginerror.html')
    return render(request, 'commonops/login.html', {'form': form})


@sensitive_post_parameters('password', 'confirm_password', 'email')
def sign_up(request):
    form = forms.CustomUserCreationForm()
    if request.method == 'POST':
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if form.cleaned_data.get('password1') != form.cleaned_data.get('password2'):
                return render(request, 'commonops/signuperror.html', {'error': 'Passwords do not match.'})
            user.save()
            return redirect('commonops:auth')
        return render(request, 'commonops/signuperror.html', {'errors': form.errors})
    return render(request, 'commonops/signup.html', {'form': form})


def change_password(request):
    form = forms.ChangePassForm()
    if request.method == "GET":
        return render(request, 'commonops/changepass.html', {'form': form})
    elif request.method == "POST":
        form = forms.ChangePassForm(request.POST)
        if form.is_valid():
            try:
                user = models.CustomUser.objects.get(email=form.cleaned_data.get('email'))
            except models.CustomUser.DoesNotExist:
                return render(request, 'commonops/changepasserror.html', {'form': form})
            subject = 'Account Password Change Request- Intranetsite.'
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
                    Intranetsite Team.
            """
            send_mail(subject, message, 'no-reply@intranet.com', [user.email], html_message=message)
            return redirect('commonops:email-sent')
        return render(request, 'commonops/changepasserror.html', {'form': form, 'errors': form.errors})


def pricing_view(request):
    return render(request, 'commonops/pricing.html', {})


def email_sent(request):
    email = request.session.get('email')
    return render(request, 'commonops/emailsent.html', {'user': email})
