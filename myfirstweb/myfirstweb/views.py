from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from login.models import people
from redisbloom.client import Client




def pages(request):
    return HttpResponse('返回结果')
def index(request):

        return render(request, 'login.html')
def checkExist(name):
    db = Client(host='hadoop101', port=6379)
    flag = db.bfExists('userinfo', "lin")
    return flag

def intpage(request, pg):

    username = request.GET.get('username')
    password = request.GET.get('password')
    #object = people.objects.filter(username=username,password=password)
    #存在返回一
    flag = checkExist(username)

    if flag == 1:
        print("用户存在")
        return HttpResponse('Get请求成功' + request.GET.get('username', 'c'))
    else:
     #引导到注册模块
     print("用户不存在")
     return HttpResponseRedirect('test_html')
def Register_Info(request):
    username = request.Get.get('username')
    password = request.Get.get('password')
    mes = request.Get.get('mes')
    object = people(username=username,password=password,mes=mes)







def test_html(request):
    t = loader.get_template('test.html')
    html = t.render()
    dic = {}
    dic['username'] = 'lin'
    dic['password'] = '****'
    dic['fun'] = get_flag()
    dic['lst'] = ['info', 'map']
    dic['dic'] = {'a': 11}
    dic['obj'] = people()
    dic['m'] = 11
    dic['x'] = 11
    dic['script'] = '<script>alert(11)</script>'
    return render(request, 'test.html', dic)


def get_flag():
    return '返回成功'
