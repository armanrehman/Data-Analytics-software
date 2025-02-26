from django.shortcuts import render
from django.http import HttpResponse
from .models import Data
import pandas as pd
import json

# Create your views here.
#sending an http response to req
def hello(request):
    if(request.method=='POST'):
        previous_data = Data.objects.all()
        previous_data.delete()
        file = (request.FILES['file'])
        df = pd.read_csv(file)
        json_records= df.reset_index().to_json(orient='records') #for numeric indexes
        data = []
        data = json.loads(json_records)
        for d in data:
            name = d['property_name']
            price = d['property_price']
            rent = d['property_rent']
            emi = d['emi']
            tax = d['tax']
            exp = d['other_exp']
            expenses_monthly = emi+tax+exp
            income_monthly= rent - expenses_monthly
            dt = Data(name=name , price=price, rent=rent,emi=emi, tax=tax, exp=exp, expenses_monthly=expenses_monthly , income_monthly= income_monthly)
            dt.save()
        data_objects = Data.objects.all()       #extract all data to pass
        context = {'data_objects': data_objects}
        return render(request,'myapp/index.html',context)

    else:
        print("This is a GET request")

    return render(request,'myapp/index.html')
