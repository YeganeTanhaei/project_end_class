from . import views
from django.urls import path
app_name='contactus'
urlpatterns=[
    path('',views.contactus_func,name='contactus-func'),
    path('register/', views.user_register,name='user-register'),
    path('login/',views.user_login,name='user-login'),
    path('logout/',views.user_logout,name='user-logout'),
]