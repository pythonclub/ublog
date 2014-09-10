from django.views.generic import DetailView, ListView
from .models import Entry


class EntryListView(ListView):
    queryset = Entry.objects.published()
    template_name = 'entry_list.html'
    paginate_by = 2


class EntryDetailView(DetailView):
    model = Entry
    template_name = 'entry_detail.html'
