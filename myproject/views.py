from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
import random
# Imaginary function to handle an uploaded file.

def handle_uploaded_file(f):
    for key, value in f:
        print(key)
        print(value)
    for filename, file in f.iteritems():
        name = f[filename].name
        with open(f"/source/{name}", "wb+") as destination:
            for chunk in f.chunks():
                destination.write(chunk)


def upload_file(request):
    if request.method == "POST":
        print("here")
        print(request.POST)
        print(request.FILES)

        form = UploadFileForm(request.POST, request.FILES)
        mdict = MultiValueDict(abc)
        qdict = QueryDict('', mutable=True)
        qdict.update(mdict)
        handle_uploaded_file(request.FILES)
        return HttpResponseRedirect("/success/url/")
    else:
        form = UploadFileForm()
    return render(request, "upload.html", {"form": form})