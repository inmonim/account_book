from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    log = str(request.user)
    if log == 'AnonymousUser':
        return redirect('users:login')

    return render(request, 'main/index.html')

def consume(request):
    return render(request, 'main/consume.html')