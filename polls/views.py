from multiprocessing.connection import answer_challenge
from tkinter import ANCHOR
from django.shortcuts import render, get_object_or_404
from .models import Question,Answer

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'polls/question_list.html', {'questions':questions})

def question_detail(request, question_id):
   question = get_object_or_404(Question, pk=question_id)
   return render(request, 'polls/question_detail.html', {'question': question})
