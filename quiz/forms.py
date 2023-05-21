from django import forms
from .models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'content']  # QuestionForm에서 사용할 Question 모델의 속성
        # widgets 속성을 지정하면 subject, content 입력 필드에 form-control과 같은 부트스트랩 클래스를 추가할 수 있다.
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        # }
        # 질문 등록 화면에 표시되는 'Subject', 'Content'를 영문이 아니라 한글로 표시하고 싶다면 다음처럼 labels 속성을 지정하면 된다.
        labels = {
            'subject': '제목',
            'content': '내용',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }
