from django.urls.conf import path
from .views import *


app_name = 'app_event_api'
urlpatterns = [
    path('create-event/', CreateEventView.as_view(), name="create_event"),
    path('edit-event/<uuid:event_id>/', EditEventView.as_view(), name='edit_event'),
    path('get-events/', RetrieveEventView.as_view(), name="get_events"),
    path('join-event/<uuid:event_id>/<uuid:user_id>/', JoinEventView.as_view(), name='join_event')
]