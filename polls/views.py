from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

#ogni funzione deve restituire HttpResponse opppure sollevare un'eccezione, 
#render fa tutta la roba dell'html e restituisce HttpResponse

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]  ##__lte sta per "less than of equal to"

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
                                                        "question": question,
                                                        "error_message": "You didn't select a choice",
                                                    })
    else:
        selected_choice.votes = selected_choice.votes + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        print(selected_choice, selected_choice.choice_text, selected_choice.votes, question.choice_set.get(pk=request.POST["choice"]))
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))