from django.shortcuts import redirect, render
from .models import Document
from .forms import DocumentForm
from django.http import JsonResponse
from django.http import HttpResponse

def uploadDocx(request):
    print(f"Great!Starting Uploading Doocx files here")
    message = 'Please Select the Document file that you want'
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return redirect('uploadDocx')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message}
    return render(request, 'list.html', context)

def  JsonTable(request):
    context={
        "title": "Table 1",
        "rows": [{
        "cells": ["Header 1", "Header 2", "Header 3"]
            },
            {
            "cells": ["Value 1", "Value 2", "Value 3"]
            },
            {
                "cells": ["Value 1", "Value 2", "Value 3"]
            }
        ]
        }

    #return render(request, 'demo.html', context)
    return JsonResponse(context)

def XMLTable(request):
    return HttpResponse(open('templates/myxmlfile.xml').read())
    
