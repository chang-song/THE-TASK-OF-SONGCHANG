from django.urls import path
from .views import user_register, user_login, update_user_info, activate_account

urlpatterns = [
    path('user/register/', user_register, name='user-register'),
    path('user/activate_account', activate_account, name='activate_account'),
    path('user/login/', user_login, name='user-login'),
    path('user/update/<int:user_id>/', update_user_info, name='update-user-info'),
    # 其他该应用程序内部的 URL 路由...
]
