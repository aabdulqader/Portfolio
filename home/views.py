from django.shortcuts import render, HttpResponse
from home.models import Contact



def home(request):
    #context = {'name': 'shimul', 'course': 'Django'}

    return render(request, 'home.html')


def about(request):

    return render(request, 'about.html')


def projects(request):


    return render(request, 'projects.html')
    
def contact(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        ins = Contact(name=name, email=email, phone=phone,desc=desc)
        ins.save()
        print('the data has been written to db')
    return render(request, 'contact.html')
   
