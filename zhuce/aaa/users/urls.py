from django.urls import path
from .views import login, confirm_code

urlpatterns = [
    path('login/', login, name='login'),
    path('confirm_code/', confirm_code, name='confirm_code'),
]