from django.urls import path

# from Insta.views import HelloDjango

from . import views

urlpatterns = [
    path('', views.HelloDjango.as_view()),
]
