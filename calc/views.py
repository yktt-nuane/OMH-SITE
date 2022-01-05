from django.shortcuts import render
from django.http import HttpResponse
from .forms import CalcPlusForm

def index(request):
    params = {
        'title':'CalcPlus',
        'forms': CalcPlusForm(),
        'answer':'Answer is '
    }
    if (request.method == 'POST'):
        params['answer'] = 'Answer is ' + str(int(request.POST['ペプタメンスタンダード']) + int(request.POST['アイソカルサポート']))
        params['kcal'] =  str(int(request.POST['ペプタメンスタンダード'])*2 + int(request.POST['アイソカルサポート'])*3) + "kcal"
        params['protein'] =  '蛋白:' + str(int(request.POST['ペプタメンスタンダード'])*0.1 + int(request.POST['アイソカルサポート'])*0.08) + "g"
        params['lipid'] =  '脂質:' + str(int(request.POST['ペプタメンスタンダード'])*0.1 + int(request.POST['アイソカルサポート'])*0.08) + "g"
        params['water'] =  '水分:' + str(int(request.POST['ペプタメンスタンダード'])*0.1 + int(request.POST['アイソカルサポート'])*0.08) + "mL"
        params['forms'] = CalcPlusForm(request.POST)
    return render(request, 'calc/calc.html', params)