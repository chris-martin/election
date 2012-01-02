from django.conf.urls.defaults import *
from django.contrib import admin
from election.bills.models import Bill

admin.autodiscover()

info_dict = {
  'queryset': Bill.objects.all(),
}

urlpatterns = patterns('',
  # Example:
  # (r'^election/', include('election.foo.urls')),

  # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
  # to INSTALLED_APPS to enable admin documentation:
  # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

  (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
)
