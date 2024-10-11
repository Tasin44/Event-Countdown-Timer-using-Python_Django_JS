from django.urls import path
from . import views
from .views import EventListView,EventDetailView

app_name='Countdownapp'

urlpatterns = [
    path('',EventListView.as_view(),name='event-list'),
    path('<pk>/',EventDetailView.as_view(),name='event-detail'),
]
