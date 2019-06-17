from django.urls import path
from .views import HomePageView, user_search, leaderboard

app_name = 'home'

urlpatterns = [
    path('', HomePageView, name='index'),
    path('search/', user_search, name='search'),
    path('leaderboard/', leaderboard, name='leaderboard')
]
