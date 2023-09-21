from .import views
from django.urls import path

urlpatterns = [
    path("chat/", views.ChatModalView.as_view()),
    path("runquery/", views.RunQueryView.as_view()),
    # path("workflow/", views.WorkflowModalView.as_view()),
    path("workflow/deploy", views.WorkflowDeployView.as_view())
]
