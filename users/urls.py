from django.urls import path, include
from .views import UserList, UserDetail

urlpatterns = [
  path('', include('djoser.urls')),
  path('', include('djoser.urls.authtoken')),
  path('users/', UserList.as_view(), name='user-list'),
  path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]