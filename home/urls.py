from django.urls import path
from home.views import home, contact, stories
# from . import views

urlpatterns = [
    path('', home, name='home'),
    path('<slug:slug>/', home, name = 'home'),
    path('contact/', contact, name='contact'),
    path('stories/', stories, name='stories')
]