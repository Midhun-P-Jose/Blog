from django.urls import path
from . import views
from blogapp import views as blogappview

urlpatterns = [
    path('',blogappview.home,name = 'home'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name = 'signup'),
    path('logout/',views.acc_logout,name = 'acc_logout')
]

