from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.urls import reverse, reverse_lazy

from django.shortcuts import render

from .models import HelloWorld
from .forms import AccountUpdateForm
from .decorators import account_ownership_required

has_ownership = [login_required, account_ownership_required]

@login_required
def hello_world(request):
    if request.method == 'POST':
        # POST 요청에서 hello_world_input 값만 가져 온다.
        temp = request.POST.get('hello_world_input')
        # HelloWorld 모델을 이용해 DB에 저장
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        # HelloWorld 타입 객체 전부 불러오기
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': 'hello_world_list'})        

        
class AccountCreateView(CreateView):
    #회원 가입 뷰
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    #마이 페이지 뷰
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    #회원 정보 수정 뷰
    model = User
    form_class = AccountUpdateForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    #회원 탈퇴 뷰
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'