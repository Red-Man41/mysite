from django.urls import path
from . import views

from . import views #senza questo non va un cazzo

app_name = "polls" 
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("question/<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("question/<int:pk>/results/", views.ResultView.as_view(), name="results"),
    path("question/<int:question_id>/vote/", views.vote, name="vote"),
]