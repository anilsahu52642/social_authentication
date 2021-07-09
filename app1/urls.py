from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.signup,name='signup_page'),
    path('signin/',views.signin,name='signin_page'),
    path('profile/',views.profile,name='profile_page'),
    path('logout/',views.mylogout,name='logout_page'),

]