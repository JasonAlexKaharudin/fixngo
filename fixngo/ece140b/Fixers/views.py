from django.http.response import Http404
from django.shortcuts import redirect, render
from fixngo.models import s_RepairRequest, h_RepairRequest

# Create your views here
def dashboard(request):
    s_repair_list = s_RepairRequest.objects.filter(is_taken = False)
    h_repair_list = h_RepairRequest.objects.filter(is_taken = False)
    context = {'software': s_repair_list, 'hardware': h_repair_list}
    return render(request, 'Fixers/dashboard.html', context)

def finishSoftJob(request, job_id):
    try:
        job = s_RepairRequest.objects.get(pk=job_id)
        job.is_Fixed = True
        job.save()
        return redirect('/jobs')
    except s_RepairRequest.DoesNotExist:
        raise Http404("Request does not exist")
    

def finishHardJob(request, job_id):
    try:
        job = h_RepairRequest.objects.get(pk=job_id)
        job.is_Fixed = True
        job.save()
        return redirect('/jobs')
    except s_RepairRequest.DoesNotExist:
        raise Http404("Request does not exist")

def jobs(request):
    s = s_RepairRequest.objects.filter(is_taken = True)
    h = h_RepairRequest.objects.filter(is_taken = True)

    return render(request, 'Fixers/jobs.html', {'software': s, 'hardware': h})

def software_jobs(request, job_id):
    try:
        job = s_RepairRequest.objects.get(pk=job_id)
        job.is_taken = True
        job.save()
        return redirect('/jobs')
    except s_RepairRequest.DoesNotExist:
        raise Http404("Job does not exist")

def hardware_jobs(request, job_id):
    try:
        job = h_RepairRequest.objects.get(pk=job_id)
        job.is_taken = True
        job.save()
        return redirect('/jobs')
    except h_RepairRequest.DoesNotExist:
        raise Http404("Job does not exist")
