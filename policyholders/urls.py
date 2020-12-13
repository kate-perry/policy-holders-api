from django.conf.urls import url 
from policyholders import views 
 
urlpatterns = [ 
    url(r'^api/policyholders$', views.policyholder_list),
    url(r'^api/policyholders/(?P<pk>[0-9]+)$', views.policyholder_detail)
]