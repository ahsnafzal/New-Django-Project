from .views import SaveVoicesView, VoicesListView, GenerateAudioView
from django.urls import path

urlpatterns = [
    path("voices/", VoicesListView.as_view()),
    path("audio/", GenerateAudioView.as_view())
]