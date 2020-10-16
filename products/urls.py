from django.conf.urls import url

from products import views

urlpatterns = [
    url(r'^api/products$', views.product_list),
    url(r'^api/products/(?P<pk>[0-9]+)$', views.product_detail),
]
