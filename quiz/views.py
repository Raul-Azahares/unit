from django.shortcuts import render, redirect, render_to_response
from django.views.generic import ListView,TemplateView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext

from .models import *



class QuizListView(ListView):
    model = Question
    template_name = 'quiz_list.html'


class AnswerView(CreateView):
    model = Answer
    fields = ['text']
    template_name = 'answer_form.html'
    success_url = reverse_lazy("validate_quiz")

    def form_valid(self, form):
        answer = form.save(commit=False)
        question = Question.objects.get(id=self.kwargs['pk'])
        print form.cleaned_data['text']
        print question.answer.text
        if question.answer.text == form.cleaned_data['text']:
            return redirect('/quiz/validar/')
        else:
            return render_to_response("invalida_quiz.html", {"id": self.kwargs['pk']},)



class ValidateView( TemplateView):
    template_name = 'validate_quiz.html'

class InvalidaView( TemplateView):
    template_name = 'invalida_quiz.html'