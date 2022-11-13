from multiprocessing.connection import answer_challenge
from random import choices
from tkinter import ANCHOR
from django.shortcuts import render, get_object_or_404
from .models import Choice, Question

from django.urls import reverse
from django.http import HttpResponseRedirect

from .forms import QuestionForm
from .forms import ChoiceForm

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'polls/question_list.html', {'questions':questions})

def question_detail(request, question_id):
   question = get_object_or_404(Question, pk=question_id)
   return render(request, 'polls/question_detail.html', {'question': question})

def question_add(request):
   if request.method == 'POST':
       form = QuestionForm(request.POST)

       if form.is_valid():
           form.save()
           return HttpResponseRedirect(reverse('polls:question_list'))

   else:
       form = QuestionForm()
       return render(request, 'polls/question_form.html', {'form': form})

def choice_list(request):
    choices = Choice.objects.all()
    return render(request, 'polls/choice_list.html', {'choices':choices})

def choice_add(request):
   if request.method == 'POST':
       form = ChoiceForm(request.POST)

       if form.is_valid():
           form.save()
           return HttpResponseRedirect(reverse('polls:choice_list'))

   else:
       form =ChoiceForm()
       return render(request, 'polls/choice_form.html', {'form': form})

