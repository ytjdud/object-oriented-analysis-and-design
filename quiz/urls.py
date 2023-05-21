from django.urls import path

from . import views

app_name = 'quiz'

urlpatterns = [
    # name: url 수정 시 용이성 위해 별칭 부
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
]
