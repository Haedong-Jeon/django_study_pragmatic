from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.urls import reverse, reverse_lazy

from django.views.generic import CreateView

from django.shortcuts import render

from .models import HelloWorld

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
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'