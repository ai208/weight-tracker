from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('mypage/',views.MypageView.as_view(),name='mypage')
]
