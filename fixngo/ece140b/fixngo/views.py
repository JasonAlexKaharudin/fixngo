from django.shortcuts import render
from django.http.response import Http404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import s_RepairRequest, h_RepairRequest
from django.contrib.auth.models import User

from datetime import datetime
from .forms import UserRegisterForm


# Create your views here.
# static views
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created for {username}! Please Login') 
            return redirect('/login')
    else:
        form = UserRegisterForm()
    return render(request, 'fixngo/register.html', {'form': form})


def home(request):
    return render(request, 'fixngo/home.html')

@login_required
def profile(request):
    return render(request, 'fixngo/profile.html')


@login_required
def software(request):
    if request.method == 'POST':
        repair_name = request.POST['repair_name']
        os = request.POST['OS']
        info = request.POST['info']
        postalcode = request.POST['postalcode']
    
        newRepair = s_RepairRequest(
            Customer = request.user, pub_date = datetime.now(),
            repair_name=repair_name, description = info, operating_system = os,
            customer_postalCode = postalcode
        )
        newRepair.save()
        return redirect('/myrepairs')
        
    return render(request, 'fixngo/software.html')

def soft_review(request, repair_id):
    try:
        sRequest = s_RepairRequest.objects.get(pk=repair_id)
    except s_RepairRequest.DoesNotExist:
        raise Http404("Request does not exist")
    return render(request, 'fixngo/soft_review.html', {'request': sRequest})

def hard_review(request, repair_id):
    try:
        hRequest = h_RepairRequest.objects.get(pk=repair_id)
    except h_RepairRequest.DoesNotExist:
        raise Http404("Request does not exist")
    return render(request, 'fixngo/hard_review.html', {'request': hRequest})

def soft_post_review(request, repair_id):
    s = s_RepairRequest.objects.get(pk=repair_id)
    if request.method == "POST":
        review = request.POST['review']
        s.review = review
        s.save()
        return redirect('/myrepairs')

def hard_post_review(request, repair_id):
    h = h_RepairRequest.objects.get(pk=repair_id)
    if request.method == "POST":
        review = request.POST['review']
        h.review = review
        h.save()
        return redirect('/myrepairs')


@login_required
def s_repair_detail(request, repair_id):
    try:
        sRequest = s_RepairRequest.objects.get(pk=repair_id)
    except s_RepairRequest.DoesNotExist:
        raise Http404("Request does not exist")
    return render(request, 'fixngo/s_detail.html', {'request': sRequest})


@login_required
def hardware(request):
    if request.method == 'POST':
        repair_name = request.POST['repair_name']
        device = request.POST['device']
        info = request.POST['info']
        postalcode = request.POST['postalcode']
    
        newRepair = h_RepairRequest(
            Customer = request.user, pub_date = datetime.now(),
            repair_name=repair_name, description = info,
            device = device ,customer_postalCode = postalcode
        )
        newRepair.save()
        return redirect('/myrepairs')
        
    return render(request, 'fixngo/hardware.html')

@login_required
def h_repair_detail(request, repair_id):
    try:
        hRequest = h_RepairRequest.objects.get(pk=repair_id)
    except h_RepairRequest.DoesNotExist:
        raise Http404("Request does not exist")
    return render(request, 'fixngo/h_detail.html', {'request': hRequest})


@login_required
def repairs(request):
    curr_user = request.user.id
    s_repair_list = s_RepairRequest.objects.filter(Customer = curr_user)
    h_repair_list = h_RepairRequest.objects.filter(Customer = curr_user)
    context = {'software': s_repair_list, 'hardware': h_repair_list}
    return render(request, 'fixngo/myrepairs.html', context)


