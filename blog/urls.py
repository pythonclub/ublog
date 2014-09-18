from django.conf.urls import patterns, url
from .feed import LatestEntryFeed
from .views import EntryListView, EntryDetailView


urlpatterns = patterns(
    '',
    url(r'^$', EntryListView.as_view(), name='home'),
    url(r'^(?P<slug>\S+)$', EntryDetailView.as_view(), name='detail'),
    url(r'^latest/feed/$', LatestEntryFeed(), name='feed'),
)
