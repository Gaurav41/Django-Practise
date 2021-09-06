from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import FileUploadForm
from django.core.files.storage import FileSystemStorage
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