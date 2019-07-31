from django.urls import path
from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from credentials.views import user_management, activities

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html') , name= "home"),
    path('login', user_management.login, name='login'),
    path('logout', user_management.logout, name='logout'),
    path('signup', user_management.register, name='register'),

    url(r'^activities', activities.show_activities.as_view(), name='activities'),

]
