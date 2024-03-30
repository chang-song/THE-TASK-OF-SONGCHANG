# anime_collection/urls.py (子路由)

from django.urls import path
from .views import (anime_list, add_to_favorites,  add_rating, update_status, add_comment, favorites,  delete_friend,
                    add_friend,  friend_request,  my_friends)


urlpatterns = [
    path('anime_list/', anime_list, name='anime_list'),
    path('add_to_favorites/<int:anime_id>/', add_to_favorites, name='add_to_favorites'),
    path('add_rating/<int:favorite_id>/', add_rating, name='add_rating'),
    path('update_status/<int:favorite_id>', update_status, name='update_status'),
    path('add_comment/<int:favorite_id>', add_comment, name='add_comment'),
    path('favorites/', favorites, name='favorites'),
    # 删除好友
    path('delete_friend/<int:friend_id>/', delete_friend, name='delete_friend'),
    # 加好友
    path('add_friend/<int:friend_id>/', add_friend, name='add_friend'),
    # 好友申请
    path('friend_request/', friend_request, name='friend_request'),
    # 查看我的好友
    path('my_friends/', my_friends, name='my_friends'),
]


