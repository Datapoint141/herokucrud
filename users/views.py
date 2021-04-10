from django.shortcuts import render,HttpResponse
from tensorflow.contrib.learn.python.learn.estimators.composable_model import LinearComposableModel

from .models import StudentModels,ProductsModels
from .forms import ProductForms
from django.conf import settings
# Create your views here.

def userRegisterForm(request):
    return render(request,'register.html',{})

def StudentRegistrations(request):
    sname = request.POST.get('studentname')
    htno = request.POST.get('Hallticket')
    s_email = request.POST.get('Email')
    s_address = request.POST.get('Address')
    s_mobile = request.POST.get('Mobile')
    StudentModels.objects.create(studentName=sname,Hallticket=htno,Mobile=s_mobile,Email=s_email,Address=s_address)

    return render(request,'register.html',{'msg':"Registration success"})

def ViewRegistrations(request):
    data = StudentModels.objects.all()
    return render(request,'ViewRegistration.html',{'data':data})

def productviews(request):
    if request.method=='POST':
        form = ProductForms(request.POST)
        if form.is_valid():
            form.save()
            print('Data Stored')
            form = ProductForms()
            return render(request, 'Products.html', {'form': form,'msg':'Product Created'})
        else:
            print('Invalid data')
    else:
        form = ProductForms()
        return render(request,'Products.html',{'form':form})

def viewProducts(request):
    data = ProductsModels.objects.all()
    return render(request,'ViewProducts.html',{'data':data})

def StartRegression(request):
    filepath = settings.MEDIA_ROOT+"\\"+ 'Salary_Data.csv'
    print('File Path',filepath)
    import pandas as pd
    df = pd.read_csv(filepath)
    print(df.head())
    X = df.iloc[:, :-1].values
    y = df.iloc[:, 1].values
    from sklearn.model_selection import train_test_split
    X_train, X_test,y_train,y_test = train_test_split(X,y,test_size=0.30,random_state=0)
    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit(X_train,y_train)
    y_pred = model.predict(X_test)
    print('Prediction Salary ',y_pred)
    print('Original Salary ',y_test)
    v = 1.8
    v_pre = model.predict([[v]])
    print('Mangalam Salary :',v_pre)


    return HttpResponse('We are in Hell of the machine Learning Code')