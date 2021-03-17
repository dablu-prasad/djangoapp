import datetime
from django.template import loader
from reportlab.pdfgen import canvas
import myapp
from myapp.functions.function import handle_uploaded_file
from myapp import form
from myapp.form import EmpForm, EmployeeForm
from django.shortcuts import render, redirect
from myapp.form import StudentForm

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods


def hello(request):
    return HttpResponse("<h2>Hello,Welcome to Django!</h2>")


def hello1(request):
    return HttpResponse("<h2>My Name is Dablu:<h2>")


def index(request):
    now = datetime.datetime.now()
    html = "<html><body><h3>Now time is :%s</h3></body></html>" % now
    return HttpResponse(html)


def index5(request):
    a = 1
    if a:
        return HttpResponseNotFound('<h1>Page not Found</h1>')
    else:
        return HttpResponse('<h1>Page was found</h1>')


@require_http_methods(["GET"])
def show(request):
    return HttpResponse('<h1>This is Http GET request</h1>')


def index1(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def index2(request):
    template = loader.get_template('index.html')
    name = {'student': 'rahul'}
    return HttpResponse(template.render(name))


def index3(request):
    return render(request, 'index.html')


def index(request):
    stu = EmpForm()
    return render(request, "index.html", {'form': stu})


def emp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                return redirect('/')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'index.html', {'form': form})


def index(request):
    if request.method == 'POST':
        student = StudentForm(request.POST, request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File uploaded successfuly")
    else:
        student = StudentForm()
        return render(request,"index.html",{'form':student})

def getpdf(request):
        response=HttpResponse(content_type='application/pdf')
        response['Content-Dispostion']='attachment;filename="file.pdf'
        p=canvas.Canvas(response)
        p.setFont("Times-Roman",55)
        p.drawString(100,700,"Hello,Javatpoint.")
        p.showPage()
        p.save()
        return response