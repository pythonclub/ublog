from django.views.generic import ListView
from .models import Entry


class EntryListView(ListView):
    queryset = Entry.objects.published()
    template_name = 'entry_list.html'
    paginate_by = 2
