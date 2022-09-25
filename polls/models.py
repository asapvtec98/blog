from django.db import models

class Question(models.Model):
    def __str__(self):
        return self.question_text
    class QuestionType(models.TextChoices):
        CLOSED = "Zamknięte"
        OPEN = "Otwarte"
        

    question_text = models.CharField(max_length=200, null=True)
    question_type = models.CharField(max_length=200, choices=QuestionType.choices, default=QuestionType.CLOSED)
    pub_date = models.DateTimeField('date published')
    

class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
   

class Answer(models.Model):
    def __str__(self):
        return self.answer_text

    answer_text = models.CharField(max_length=200, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    