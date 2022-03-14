"""storeapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from home.views import home_view,signupnews_view
from signups.views import signup_view,SignupView
from logins.views import login_view
from posts.views import allpost_view,search_view,ratings_views,logout
from rest_framework.urlpatterns import format_suffix_patterns
from profiles.views import profiles_view,ProjectViews,UserbioView,RatedView,save_projectView,save_bioView
from django.contrib.staticfiles.urls import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name = "homepage"),
    path('signup_to_newslater/', signupnews_view, name = "newslaters"),
    path('login/', login_view, name = "logins"),
    path('rarings/', ratings_views, name = "projratings"),
    path('register/', signup_view, name = "signups"),
    path('allposts/', allpost_view, name = "projects"),
    path('profile/', profiles_view, name = "profile"),
    path('search/', search_view, name = "search"),
    path('save_project/', save_projectView, name = "saveproject"),
    path('save_bio/', save_bioView, name = "savebio"),
    path('logout/',logout,name= 'logout'),
    path('get_projects/', ProjectViews.as_view()),
    path('get_bios/', UserbioView.as_view()),
    path('get_ratings/', RatedView.as_view()),
    path('get_registreation/', SignupView.as_view(), name="userregister"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
