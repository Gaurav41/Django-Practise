from django.http.response import HttpResponse
from django.shortcuts import render

from .forms import NameForm,CustomerForm
from .models import Customer

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            
            name = form.cleaned_data['your_name']
            # redirect to a new URL:
            # name="sd"
            return HttpResponse(f'thanks {name}')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'form_demo/name.html', {'form': form})


def req_res(request):
    print(request.scheme)
    scheme = request.scheme
    body = request.body
    path = request.path  # /form/req_res
    method = request.method
    content_type = request.content_type
    COOKIES = request.COOKIES
    META = request.META
    session = request.session
    return HttpResponse(f" Scheme: {scheme}, body: {body},path: {path} method: {method}, content_type: {content_type}, \
    COOKIES: {COOKIES}, session: {session}") 


def customer(request):
    
    if request.method == 'POST':
        # update
        # pi = Customer.objects.get(pk=5)
        # form = CustomerForm(request.POST,instance=pi)
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()

            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # email = form.cleaned_data['email']
            # password = form.cleaned_data['password']


        #   create
        #   c = Customer(first_name,last_name,email,password)
        #   c.save()

        #   update
            # c = Customer(id=1,first_name=first_name,last_name=last_name,email=email,password=password)
        #   c.save()
        #   delete

            # c = Customer(id=1,first_name=first_name,last_name=last_name,email=email,password=password)
            # c.delete()
            
            return HttpResponse("Thanks")
        else:
            return render(request, 'form_demo/customer.html',{'form':form})
            # return HttpResponse("error")

    else:
        form = CustomerForm()
        return render(request, 'form_demo/customer.html',{'form':form})
    

    