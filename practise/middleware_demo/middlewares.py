
from django.http.response import HttpResponse


def my_middleware(get_response):
    print("One Time Initialization")
    def my_function(request):
        print("This is before view")
        response = get_response(request)
        print("This is after view")
        return response
    return my_function

class MyMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        # One time initialization
        print("class based middleware")
        print("One Time Initialization of class Based middleware")

    def __call__(self,request):
        print("This is before view (class based middleware)")
        response=self.get_response(request)
        print("This is Ater view (class based middleware)")
        return response


class MyViewMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        # One time initialization
        print("Process view middleware")

    def __call__(self,request):
        print("This is before view (Process view middleware)")
        response=self.get_response(request)
        print("This is Ater view (Process view middleware)")
        return response

    def process_view(request,*args,**kwargs):
        print("This is a process view-Before View")
        
        # then return view or next middleware
        # return None;  

        # return this response instead of requested view
        return HttpResponse("This is a process view middleware response")

    

class MyExceptionMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        # One time initialization
        print("My Exception middleware")

    def __call__(self,request):
        response=self.get_response(request)
        return response

    def process_exception(self,request,exception):
        print("Exception occured")
        msg = exception
        class_name = exception.__class__.__name__ 
        print(class_name)
        print(msg)
        return HttpResponse(f"{class_name}: {msg} ")

class MyTemplateResponseMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        # One time initialization
        print("process template response middleware")

    def __call__(self,request):
        print("This is before view")
        response=self.get_response(request)
        print("This is Ater view ")
        return response

    def process_template_response(self,request,response):
        print("Process template response from middleware")
        response.context_data['name']="Data Changed"
        return response


class MyCombinedMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        # One time initialization
        print("Combined middleware")

    def __call__(self,request):
        print("This is before view")
        response=self.get_response(request)
        print("This is Ater view ")
        return response

    def process_view(request,*args,**kwargs):
        print("This is a process view-Before View")
        
        # # return view or next middleware
        return None;  

        # # return this response instead of requested view
        # return HttpResponse("This is a process view middleware response")
        
    def process_exception(self,request,exception):
        print("Exception occured")
        msg = exception
        class_name = exception.__class__.__name__ 
        print(class_name)
        print(msg)
        return HttpResponse(f"{class_name}: {msg} ")

    def process_template_response(self,request,response):
        print("Process template response from middleware")
        response.context_data['name']="Data Changed"
        return response