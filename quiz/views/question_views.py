from django.utils import timezone

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from quiz.forms import AnswerForm, QuestionForm
from quiz.models import Question
from django.contrib import messages


@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(
                commit=False)  # 임시 저장하여 question 객체를 리턴받는다. 아직 create_date 에 대한 정보가 없어서 실제 DB 에 저장할 수 없기 때문.
            question.author = request.user  # author 속성에 로그인 계정 저장
            question.create_date = timezone.now()  # 실제 저장을 위해 작성일시를 설정한다.
            question.save()  # 데이터를 실제로 저장한다.
            return redirect('quiz:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'quiz/question_form.html', context)


# question_modify 함수는 로그인한 사용자(request.user)와 수정하려는 질문의 글쓴이(question.author)가 다를 경우에는
# "수정권한이 없습니다"라는 오류를 발생시킨다. 이 오류를 발생시키기 위해 messages 모듈을 이용하였다.
@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('quiz:detail', question_id=question.id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('quiz:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'quiz/question_form.html', context)


@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('quiz:detail', question_id=question.id)
    question.delete()
    return redirect('quiz:index')


@login_required(login_url='common:login')
def question_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다')
    else:
        question.voter.add(request.user)
    return redirect('quiz:detail', question_id=question.id)
