from django.conf.urls import patterns, url
from .views import EntryListView


urlpatterns = patterns(
    '',
    url(r'^$', EntryListView.as_view(), name="home"),
)
