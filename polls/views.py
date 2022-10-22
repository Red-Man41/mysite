from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse

from .models import Question, Choice

#ogni funzione deve restituire HttpResponse opppure sollevare un'eccezione, 
#render fa tutta la roba dell'html e restituisce HttpResponse

def index(request):
    latest_question_list = get_list_or_404(Question)
    latest_question_list.reverse()
    latest_question_list = latest_question_list[:5]   #len(latest_question_list)-5:len(latest_question_list)
    template = loader.get_template("polls/index.html")
    context = {
                    "latest_question_list": latest_question_list,
              }
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
                    "question":question
              }
    print(context)
    return render(request, "polls/detail.html", context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

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
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))