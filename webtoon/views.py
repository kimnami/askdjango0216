from django.shortcuts import redirect, render
from .models import Webtoon
import json
from django.http import HttpResponse
from .forms import PostForm
from django.http import JsonResponse
import time

def count_web(request):
    if request.method == 'POST':
        #POST goes here . is_ajax is must to capture ajax requests. Beginner's pit.
        if request.is_ajax():
            data = request.POST.get('webtitle','')
            return JsonResponse(data)
    #Get goes here
    return render(request,'webtoon/webtoon_list.html')

def webtoon_list(request):
    q = request.GET.get('q','') #q가 없으면 ''를 보여줌
    qs = Webtoon.objects.all()
    webtoon_list = qs

    if q:
        webtoon_list = Webtoon.objects.all().filter(title__contains=q)

    content={'qs':qs, 'webtoon_list':webtoon_list,'q' : q,'count' :Webtoon.objects.all().count()}


    return render(request, 'webtoon/webtoon_list.html',content)

def webtoon_detail(request, id):
    webtoon = Webtoon.objects.get(id=id)
    return render(request, 'webtoon/webtoon_detail.html',{'webtoon':webtoon})



def get_title(request):
    if request.is_ajax():
        q = request.GET.get('term','')
        webtoon_list = Webtoon.objects.all().filter(title__contains = q)
        results = []
        for webtoon in webtoon_list:
            webtoon_json = {}
            webtoon_json['id'] = webtoon.id
            webtoon_json['label'] = webtoon.title
            webtoon_json['value'] = webtoon.title
            results.append(webtoon_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def counter(request):
    if request.is_ajax():
        time.sleep(2)
        data = {}
        data['cnt'] = Webtoon.objects.all().count()
        data = json.dumps(data)

    return HttpResponse(data)

