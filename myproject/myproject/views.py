from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .form import userForms

def homePage(request):
    return render(request,"index.html")

def aboutUs(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def portfolio(request):
    return render(request, "portfolio.html")

def sevices(request):
    return render(request, "services.html")

def demo(request):
    data={
'title':'Home Page',
        'clist':['HTML','CSS','React JS','Python'],
        'student_details':[
        {'Name':'Shaukat','Phone': 1234567891},
        {'Name':'Avez','Phone': 1234567891},
        {'Name':'Tushar','Phone': 1987654321}
        ],
        'numbers':[10,50,40,80.99,55,33,19]
    }
    return render(request, "demo.html", data)

# def courseDetails(request, courseId):
#     return HttpResponse(courseId)

# def product(request, productName):
#     return HttpResponse(productName)


# GET Method 
# def form(request):
#     final = ""
#     try:
#         n1 = int(request.GET.get('num1'))
#         n2 = int(request.GET.get('num2'))
#         final = n1+n2
#     except:
#         pass
#     return render(request, "form.html", {'output':final})

# POST Method 
def form(request):
    final = ""
    try:
       if request.method == "POST":
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            final = n1+n2
            # Form Redirection 
            return HttpResponseRedirect('/')
    except:
        pass
    return render(request, "form.html", {'output':final})

# POST Method 
# def submitform(request):
#     try:
#        if request.method == "POST":
#             n1 = int(request.POST.get('num1'))
#             n2 = int(request.POST.get('num2'))
#             final = n1+n2
#             return HttpResponse(final)
#     except:
#         pass
#     return render(request, "form2.html")


def submitform(request):
    final=''
    fn= userForms()
    data={'form':fn}
    try:
        if request.method == 'POST':
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            email = request.POST.get('email')
            final= ['Num1= ',n1,"<br>" ,"Num2= ", n2, "<br>" ,"Email= " ,email]
            data={
                'form':fn,
                'output':final
            }
            return HttpResponse(final)
    except:
        pass
    return render(request, 'form2.html', data)