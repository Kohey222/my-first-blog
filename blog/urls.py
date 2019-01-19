import django.contrib.auth.views
from django.urls import path,include
from . import views
app_name='blog'

urlpatterns=[
    path('user/top/',views.top_page, name="top"), # リダイレクト
    path('user/login/', # ログイン
         django.contrib.auth.views.login,
         {
             'template_name': 'blog/login.html',
         },
         name='login'),
    path('user/logout/', # ログアウト
         django.contrib.auth.views.logout,
         {
             'template_name': 'blog/logout.html',
         },
         name='logout'),
]
