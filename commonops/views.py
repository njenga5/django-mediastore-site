import hashlib
from django.shortcuts import render, redirect, reverse
from django.utils import timezone
from django.core.mail import send_mail
from django.views.decorators.debug import sensitive_post_parameters
from . import models, forms


def home_view(request):
    return render(request, "commonops/index.html",)


def show_video(request, vid_id):
    return render(request, "commonops/video.html", {"vid_id": vid_id})

@sensitive_post_parameters()
def login(request):
    form = forms.LoginForm()
    if request.method == 'GET':
        if request.session.has_key('user'):
            return redirect('dashboard:profile')
        else:
            return render(request, 'commonops/login.html', {'form': form})
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            try:
                user = models.User.objects.get(email=request.POST['email'], password=hashlib.md5(request.POST['password'].encode()).hexdigest())
            except models.User.DoesNotExist:
                return render(request, 'commonops/loginerror.html', {'form': form})
            try:
                del request.session['email']
            except KeyError:
                pass
            request.session['user'] = user.email
            return redirect('dashboard:profile')
        return render(request, 'commonops/login.html', {'form': form})
    
@sensitive_post_parameters('password', 'confirm_password', 'email')            
def sign_up(request):
    form = forms.SignUpForm()
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            data = request.POST
            user.first_name = data['first_name']
            user.middle_name = data['middle_name']
            user.last_name = data['last_name']
            user.phone_number = data['phone_number']
            user.date_of_birth = data['date_of_birth']
            user.email = data['email']
            user.password = hashlib.md5(data['password'].encode()).hexdigest()
            user.date_joined = timezone.now()
            if data['password'] != data['confirm_password']:
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
                user = models.User.objects.get(email=request.POST['email'])
            except models.User.DoesNotExist:
                return render(request, 'commonops/changepasserror.html', {'form': form})
            subject = 'Account change password - Intranet.'
            message = f"""
                You have requested to change your account's password.
                Please click the link below to confirm.<br><br>
                <a href="http://localhost:8000/commonops/auth/"> Change Password.</a>
                <br><br><br>
                Don't recognize this action? Change your password immediately.
                Learn how to secure your account. <a href="http://localhost:8000/commonops/auth/">Learn more.</a><br><br><br><br>
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


def pricing_view(request):
    return render(request, 'commonops/pricing.html', {})

def email_sent(request):
    email = request.session.get('email')
    return render(request, 'commonops/emailsent.html', {'user': email})

