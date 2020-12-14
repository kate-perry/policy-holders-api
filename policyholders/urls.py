from django.conf.urls import url
from policyholders import views
 
urlpatterns = [ 
    url(r'^api/policyholders$', views.policyholder_list),
    url(r'^api/policyholders/(?P<pk>[0-9]+)$', views.policyholder_detail),
    url(r'^api/insuredevents$', views.insuredevent_list),
    url(r'^api/insuredevents/(?P<pk>[0-9]+)$', views.insuredevent_detail),
    url(r'^api/insuredevents/(?P<pk>[0-9]+)$', views.insuredevent_list_by_policyholder),
]