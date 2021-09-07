from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .forms import FileUploadForm, BookForm
from django.core.files.storage import FileSystemStorage
from .models import Book

# Create your views here.
def index(request):
    context = {}
    if request.method == 'POST':
        form = FileUploadForm(request.POST,request.FILES)
        if form.is_valid():
            uploded_file = request.FILES['file']
            print(uploded_file.name)
            print(uploded_file.size)

            # Save file in media directory
            fs = FileSystemStorage()
            name = fs.save(uploded_file.name,uploded_file)
            print(name)
            url = fs.url(name)
            # return HttpResponse("Thanks")
            context = { 'form': form,'url':url}
    else:
        context = { 'form': FileUploadForm()}
    
    return render(request,"file_upload/index.html",context)


def book_list(request):
    books = Book.objects.all()
    return render(request,'file_upload/book_list.html',{'books':books})

def upload_book(request):
    if request.method == "POST":
        form = BookForm(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            return redirect(book_list)
    
    else:
        form = BookForm()
        context = {'form':form}
        return render(request,'file_upload/upload_book.html',context)

def delete_book(request,pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect(book_list)
    
