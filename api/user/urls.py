from django.urls import path

from . import views

urlpatterns = [
    path('social/login/', 
         views.SocialUserLoginAPIView.as_view(), 
         name='social_login'
    ),
]
