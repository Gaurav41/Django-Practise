from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import datetime,timedelta

# Cookies
def set_cookie(request):
    response = render(request,'cookie/set_cookie.html')
    # response.set_cookie("name","Gaurav")
    # response.set_cookie("name","Gaurav",max_age=60) # 60 sec
    # response.set_cookie("name","Gaurav",expires=datetime.utcnow()+timedelta(days=2)) 
    return response

def get_cookie(request):
    # name = request.COOKIES['name']
    name = request.COOKIES.get('name') # return None if not found ... default= None 
    return render(request,'cookie/get_cookie.html',{'name':name})

def del_cookie(request):
    response = render(request,'cookie/get_cookie.html')
    response.delete_cookie("name")
    print(request.COOKIES.get('name',"deleted") )
    return response

def set_signed_cookie_(request):
    response = render(request,'cookie/set_cookie.html')
    response.set_signed_cookie("name","Gaurav",salt="xrvcs", expires=datetime.utcnow()+timedelta(days=2)) # 
    return response

def get_signed_cookie_(request):
    name = request.get_signed_cookie('name',salt="xrvcs") 
    return render(request,'cookie/get_cookie.html',{'name':name})

#   Session

def set_session(request):
    request.session['name']='Gaurav'
    return render(request,'session/set_session.html')

def get_session(request):
    name = request.session['name']
    # name = request.session.get('name',default="hkjhkjdf") # return None if not found ... default= None 
    
    keys = request.session.keys()
    items = request.session.items()

    print("Keys: ")
    for k in keys:
        print(k)
    
    print("Items: ")
    for i in items:
        print(i)
    
    # get age if exit else else set age to default value give
    age = request.session.setdefault('age',20)
    print("age",age)

    cookie_age = request.session.get_session_cookie_age()
    print('cookie_age: ',cookie_age)

    cookie_expiry_date = request.session.get_expiry_date()
    print('cookie_expiry_date: ',cookie_expiry_date) 

    cookie_expiry_age = request.session.get_expiry_age()
    print('cookie_expiry_age: ',cookie_expiry_age)
    
    is_expire_at_browser_close = request.session.get_expire_at_browser_close()
    print('is expiry_at_browser_close: ',is_expire_at_browser_close)

    request.session.set_expiry(600) #600 sec
    cookie_expiry_age = request.session.get_expiry_age()
    print('cookie_expiry_age: ',cookie_expiry_age)

    request.session.set_expiry(0) # expire after closing browser
    cookie_expiry_age = request.session.get_expiry_age()
    print('cookie_expiry_age: ',cookie_expiry_age)
    
    request.session.set_expiry(10)

    return render(request,'session/get_session.html',{'name':name})

def del_session(request):
    response = render(request,'session/get_session.html')
   
    # delete perticulat key value
    if 'name' in request.session:
        del request.session['name']
        print(request.COOKIES.get('name',"deleted") )

    # cleared data from database
    request.session.flush()
    request.session.clear_expired() # will cleard expired session from database

    return response

# Testing Cookie 

def settestcookie(request):
    request.session.set_test_cookie()
    return render(request,'test_cookie/set_test_cookie.html')

def checktestcookie(request):
    is_cookie_worked = True
    is_cookie_worked = request.session.test_cookie_worked()
    print("is_cookie_worked: ",is_cookie_worked)
    return render(request,'test_cookie/check_test_cookie.html',{'result':is_cookie_worked})

def deltestcookie(request):
    request.session.delete_test_cookie()
    return HttpResponse("test cookie deleted")


