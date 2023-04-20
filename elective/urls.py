"""elective URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from allauth.account.views import LoginView
from .views import user_info

#from .views import google_auth

urlpatterns = [
#    path('google-auth/', google_auth, name='google_auth'),
    path('admin/', admin.site.urls),
    path('register/',views.register,name="register"),
    path('',views.index,name="index"),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/', include('allauth.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('sem2',views.sem2,name="sem2"),
    path('sem3',views.sem3,name="sem3"),
    path('sem4',views.sem4,name="sem4"),
    path('sem5',views.sem5,name="sem5"),
    path('sem6',views.sem6,name="sem6"),
    path('sem7',views.sem7,name="sem7"),
    path('sem8',views.sem8,name="sem8"),
    path('nav',views.nav,name="nav"),
    path('card',views.card,name="card"),
    path('login',views.login,name="sem4"),
    path('course_selection', views.course_selection,name="course_selection"),
    path('faculty_dashboard', views.faculty_dashboard,name="faculty_dashboard"),
    path('importt',views.importt,name="importt"),
    path('',include("allauth.urls")),
    path('accounts/', include('social_django.urls', namespace='social')),
    path('user_info/', user_info, name='user_info'),
]
