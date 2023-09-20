from .import views
from django.urls import path

urlpatterns = [
    path("chat/", views.ChatModalView.as_view()),
    path("runquery/", views.RunQueryView.as_view()),
]
