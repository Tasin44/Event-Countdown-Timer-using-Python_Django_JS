from django.views.generic import ListView,DetailView
from .models import Event


class EventListView(ListView):
    model=Event
    template_name ='events/index.html'

class EventDetailView(DetailView):
    model=Event
    template_name='events/countdown.html'
