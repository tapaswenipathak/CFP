from django.urls import path
from home.views import HomePageView

app_name = 'home'

urlpatterns = [
    path('', HomePageView, name='index'),
]
