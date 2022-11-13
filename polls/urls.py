from django.urls import path
from . import views

app_name='polls'

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('choices/', views.choice_list, name='choice_list'),
    path('<int:question_id>/', views.question_detail, name='question_detail'),
    path('new/', views.question_add, name='question_add'),
    path('new_choice/', views.choice_add, name='choice_add')
]