from django.urls import path
from . import views

from . import views #senza questo non va un cazzo

app_name = "polls" 
urlpatterns = [
    path("", views.index, name="index"),
    path("question/<int:question_id>/", views.detail, name="detail"),
    path("question/<int:question_id>/results/", views.results, name="results"),
    path("question/<int:question_id>/vote/", views.vote, name="vote"),
]