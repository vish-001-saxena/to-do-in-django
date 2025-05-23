from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def about(request):
    context = {
        'title': 'About Us',
        'content': 'Welcome to our e-waste awareness website.'
    }
    return render(request, 'about.html', context)

