from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('login',views.login,name="login"),
    path('signup',views.signup,name="signup"),
    path('home/<int:id>',views.home,name="home"),
    path('gallery',views.gallery,name="gallery"),
    path('update/<int:id>',views.update,name="update"),
    path('changepassword/<int:id>',views.changepassword,name="changepassword"),


]