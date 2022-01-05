from django import forms

from calc.models import Nutrition

class CalcPlusForm(forms.Form):
    ペプタメンスタンダード = forms.IntegerField()
    アイソカルサポート = forms.IntegerField()



class NutritionForm(forms.ModelForm):
    class Meta:
        model = Nutrition
        fields = (
            'energy',
            'protein',
            'lipid',
        )
        

"""
ペプタメンスタンダード: 300, 10.5, 12.0, 37.5, 153, 1.1, 200



"""