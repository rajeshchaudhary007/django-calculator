from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def HomePage(request):
    if request.method == "POST":
        num1 = request.POST['number_one']
        num2 = request.POST['number_two']
        operator = request.POST['operator']
        
        if operator == '+':
            result = int(num1) + int(num2)
        elif operator =='-':
            result = int(num1) - int(num2)  

        elif operator =='*':
            result = int(num1) * int(num2)  

        elif operator =='/':
            result = int(num1) / int(num2)  


        return render(request,'home.html',{'result':result})
    return render(request,'home.html')


   