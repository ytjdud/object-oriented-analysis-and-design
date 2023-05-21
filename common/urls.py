from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    # 위 오류는 registration 디렉터리에 login.html 파일이 없음을 의미한다.
    # 앞에서 사용한 LoginView는 registration이라는 템플릿 디렉터리에서 login.html 파일을 찾는다.
    # 그런데 이 파일을 찾지 못해 오류가 발생한 것이다. 이 오류를 해결하려면 registration/login.html 템플릿 파일을 작성해야 한다.
    # 하지만 로그인은 common 앱에 구현할 것이므로 오류 메시지에 표시한 것처럼 registration 디렉터리에 템플릿 파일을 생성하기보다는 common 디렉터리에 템플릿을 생성하는 것이 좋다.
    # 이를 위해 LoginView가 common 디렉터리의 템플릿을 참조할 수 있도록 common/urls.py 파일을 다음과 같이 수정하자.

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]
