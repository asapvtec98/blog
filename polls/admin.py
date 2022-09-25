from django.contrib import admin


from .models import Answer, Question, Choice


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text","question_type","pub_date")
    list_filter =  ("pub_date","question_type","question_text")
    search_fields = ['question_text']

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("question","choice_text","pub_date","votes")
    list_filter =  ("pub_date",)
    search_fields = ["choice_text","question__question_text"]
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("question","answer_text")
    list_filter = ("pub_date",)
    search_fields = ["answer_text"]
    def question_text(self, obj):
        return obj.question.question_text




