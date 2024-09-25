from django.urls import path

from jokes.views import JokeApiView

urlpatterns = [
    path('jokes/', JokeApiView.as_view(), name='jokes_api'),
]
