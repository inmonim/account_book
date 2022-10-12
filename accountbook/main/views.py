from django.shortcuts import render, redirect
from .forms import Consumeform
from .models import Consume

# Create your views here.
def index(request):
    log = str(request.user)
    if log == 'AnonymousUser':
        return redirect('users:login')
    
    else:
        account_list = Consume.objects.all()
        context = {
            'account_list' : account_list
        }

    return render(request, 'main/index.html', context)

def consume(request):
    if request.method == 'POST':
        form = Consumeform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:index')
    
    else:
        form = Consumeform()
        context = {
            'form': form
        }

    return render(request, 'main/consume.html', context)

def detail(request, account_pk):
    account = Consume.objects.get(pk=account_pk)
    context = {
        'account' : account
    }
    return render(request, 'main/detail.html', context)