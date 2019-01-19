import django.contrib.auth.views
from django.urls import path,include
from . import views
app_name='blog'

urlpatterns=[
    path('top/',views.top_page, name="top"), # リダイレクト
    path('login/', # ログイン
         django.contrib.auth.views.login,
         {
             'template_name': 'blog/login.html',
         },
         name='login'),
    path('logout/', # ログアウト
         django.contrib.auth.views.logout,
         {
             'template_name': 'blog/logout.html',
         },
         name='logout'),
]
