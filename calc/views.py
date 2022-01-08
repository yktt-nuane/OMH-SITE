from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.http import HttpResponse
from .forms import CalcPlusForm
from calc.models import Nutrition

def index(request):
    params = {
        'title':'CalcPlus',
        'forms': CalcPlusForm(),
        'answer':'Answer is '
    }
    if (request.method == 'POST'):
        params['answer'] = 'Answer is ' + str(int(request.POST['nutritionselect']) + int(request.POST['アイソカルサポート']))
        params['energy_kcal'] =  str(int(request.POST['nutritionselect'])*2 + int(request.POST['アイソカルサポート'])*3) + "kcal"
        params['sugar_g'] =  str(int(request.POST['nutritionselect'])*2 + int(request.POST['アイソカルサポート'])*3) + "kcal"
        params['protein_g'] =  str(int(request.POST['nutritionselect'])*2 + int(request.POST['アイソカルサポート'])*3) + "kcal"
        params['lipid_g'] =  '蛋白:' + str(int(request.POST['nutritionselect'])*0.1 + int(request.POST['アイソカルサポート'])*0.08) + "g"
        params['water_mL'] =  '脂質:' + str(int(request.POST['nutritionselect'])*0.1 + int(request.POST['アイソカルサポート'])*0.08) + "g"
        params['salt_g'] =  '水分:' + str(int(request.POST['nutritionselect'])*0.1 + int(request.POST['アイソカルサポート'])*0.08) + "mL"
        params['potassium_mEq'] = CalcPlusForm(request.POST)
    return render(request, 'calc/calc.html', params)

