from django.urls import path
from home.views import HomePageView, user_search

app_name = 'home'

urlpatterns = [
    path('', HomePageView, name='index'),
    path('search/', user_search, name='search')
]
