from django.contrib.syndication.views import Feed
from .models import Entry


class LatestEntryFeed(Feed):
    title = 'PythonClub'
    link = '/latest/feed/'
    description = 'PythonClub - Blog colaborativo Python'

    def items(self):
        return Entry.objects.published()[:5]
