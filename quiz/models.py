from django.db import models

# Crea tus modelos de preguntas y respuestas para el quiz aqui.



class Answer(models.Model):
    text = models.CharField(max_length=500, verbose_name="respuesta")

    def __unicode__(self):
        return self.text

    class Meta:
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'

class Question(models.Model):
    text = models.CharField(max_length=300, verbose_name="pregunta")
    answer = models.ForeignKey(Answer, verbose_name="respuesta", null=True, blank=True)

    def __unicode__(self):
        return self.text

    class Meta:
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'