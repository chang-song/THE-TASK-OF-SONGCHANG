from django.shortcuts import render

# Create your views here.
# views.py
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
import random
import string
from django.core.mail import send_mail
from django.shortcuts import render
from .models import UserProfile
from .forms import LoginForm, AuthorizationCodeForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(username=username)
                if user.check_password(password):
                    authorization_code = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

                    # 将授权码保存到用户的 profile 中
                    profile, created = UserProfile.objects.get_or_create(user=user)
                    profile.authorization_code = authorization_code
                    profile.save()

                    # 发送授权码给用户
                    send_mail(
                        'Authorization Code',
                        f'Your authorization code: {authorization_code}',
                        'from@example.com',
                        [user.email],
                        fail_silently=False,
                    )

                    return HttpResponseRedirect('/confirm_code/')
                else:
                    return HttpResponse("Invalid username or password")
            except User.DoesNotExist:
                return HttpResponse("User does not exist")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def confirm_code(request):
    if request.method == 'POST':
        form = AuthorizationCodeForm(request.POST)
        if form.is_valid():
            authorization_code = form.cleaned_data['authorization_code']
            user = request.user
            profile = user.profile

            if profile.authorization_code == authorization_code:
                return HttpResponse("Authorization code is correct")
            else:
                return HttpResponse("Incorrect authorization code")
    else:
        form = AuthorizationCodeForm()

    return render(request, 'confirm_code.html', {'form': form})
