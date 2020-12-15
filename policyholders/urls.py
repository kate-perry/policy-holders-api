from django.conf.urls import url
from policyholders import views
 
urlpatterns = [ 
    # GET and POST one-to-multiple policy holders
    url(r'^api/policyholders$', views.policyholder_list),
    # GET a policy holder based on ID
    url(r'^api/policyholders/(?P<pk>[0-9]+)$', views.policyholder_detail),
    # GET and POST one-to-multiple insured events
    url(r'^api/insuredevents$', views.insuredevent_list),
    # GET an insured event based on ID
    url(r'^api/insuredevents/(?P<pk>[0-9]+)$', views.insuredevent_detail),
    # GET a list of insured events based on PolicyHolderId
    url(r'^api/insuredevents/bypolicyholder/(?P<fk>[0-9]+)$', views.insuredevent_by_policy_holder_list),
]