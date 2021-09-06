from django.http.response import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse

# Create your views here.
def index(request):
    return HttpResponse("Hi")


def user_info(request):
    context = { 'name': 'gaurav'}
    a = 10 / 0
    return TemplateResponse(request,'user.html',context)

def view_err(request):
    print("This is a error generating view ")
    a = 10 / 0
    return HttpResponse(f"value if a is: {a}")