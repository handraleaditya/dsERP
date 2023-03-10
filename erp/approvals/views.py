from django.shortcuts import render
from django.views import generic
from .models import Approval, Project

def approvals(request):

    # Numeric stats for context 
    num_approvals = Approval.objects.all().count()
    num_projects = Project.objects.all().count()
    num_approved_approvals = Approval.objects.filter(status__exact = 'a').count()
    num_declined_approvals = Approval.objects.filter(status__exact = 'd').count()
    num_pending_approvals = Approval.objects.filter(status__exact = 'p').count()
    
    # Books object 
    pending_approvals = Approval.objects.filter(status__exact = "p")
    accepted_approvals = Approval.objects.filter(status__exact = "a")
    declined_approvals = Approval.objects.filter(status__exact = "d")
    


    context = {
        "num_approvals" : num_approvals,
        "num_projects" :  num_projects,
        "num_approved_approvals" : num_approved_approvals, 
        "num_declined_approvals": num_declined_approvals,
        "num_pending_approvals": num_pending_approvals,
        "pending_approvals" : pending_approvals,
        "accepted_approvals" : accepted_approvals,
        "declined_approvals" : declined_approvals,

    }    
    
    return render(request, 'approvals.html', context=context,)

class approval_list_view(generic.ListView):
    model = Approval
    context_object_name = "approval_list"
    queryset = Approval.objects.filter()
    template_name = "templates/approval_list.html"  
    
    # return 0