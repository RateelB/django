from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
Tax_rate=0.15

def index(request):
    return HttpResponse("<h1>This a site to calculate tax </h1>")

def tax_cal(request,number):
    try:
       number= float(number)
       total_price= number *(1+Tax_rate)
       return HttpResponse(f"<h1>Total price after tax: ${total_price:.2f}</h1>")
    except ValueError:
        return HttpResponse(f"<h1>invalid number</h1>")

def tax_rate(request):

    return HttpRespose(f"<h1>Tax Rate: {Tax_Rate *100}%</h1>",{"Tax_rate":Tax_rate})

