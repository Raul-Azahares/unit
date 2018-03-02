from rest_framework import viewsets
from serializers import *

#NO ME DIO TIEMPO TERMINARLO POR  API REST


class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()