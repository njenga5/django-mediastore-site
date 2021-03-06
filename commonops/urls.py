from django.urls import path, re_path
from . import views


app_name = 'commonops'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('signup', views.sign_up, name='signup'),
    path('auth', views.login_view, name='auth'),
    path('oauth/change', views.change_password, name='chpass'),
    path('oauth/change/sent', views.email_sent, name='email-sent'),
    path('learn/pricing', views.pricing_view, name='pricing'),
]
