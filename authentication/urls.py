from django.conf.urls import url

from authentication import views

urlpatterns = [
    url(r'^api/register$', views.register),
    url(r'^api/login', views.login)
]
