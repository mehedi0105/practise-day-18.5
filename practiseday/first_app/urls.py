from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='homepage'),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('pass_change1/',views.pass_change1,name='pass_change1'),
    path('pass_change2/',views.pass_change2,name='pass_change2'),
]
