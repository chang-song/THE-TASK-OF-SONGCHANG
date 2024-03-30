from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from .models import User
from django.utils.http import urlsafe_base64_decode


@api_view(['POST'])
def user_register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()

        current_site = get_current_site(request)
        mail_subject = 'Activate your account'
        message = render_to_string('activation_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': user.activation_code,
        })
        to_email = user.email
        send_mail(mail_subject, message, 'from@example.com', [to_email])

        return Response("Please check your email to activate your account.")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def activate_account(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
        if user.activation_code == token:
            user.is_active = True
            user.save()
            return Response("Account activated successfully.")
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        pass
    return Response("Activation link is invalid.")


@api_view(['POST'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    try:
        user = User.objects.get(username=username, password=password)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response("Invalid username or password", status=status.HTTP_401_UNAUTHORIZED)


@api_view(['PUT'])
def update_user_info(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response("User not found", status=status.HTTP_404_NOT_FOUND)
