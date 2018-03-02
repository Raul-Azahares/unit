from django.conf.urls import url
from views import *
urlpatterns = [
            url(r'^$', QuizListView.as_view(), name='quiz_list'),
            url(r'^responder/(?P<pk>\d+)$', AnswerView.as_view(), name='answer_quiz'),
            url(r'^validar/', ValidateView.as_view(), name='validate_quiz'),
            url(r'^invalida/', InvalidaView.as_view(), name='invalida_quiz'),

]