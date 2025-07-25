from django.shortcuts import render,redirect
from .models import Contact

# Create your views here.
def home(req):
    return render(req,'home.html')


def about(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )


    return render(request,'about.html')



def projects(req):
    return render(req,'projects.html')



def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save to database
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        return redirect('home')  
    return render(request, 'signup.html')




