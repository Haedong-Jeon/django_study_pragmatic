from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
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