from django.shortcuts import render, redirect
from visitors.models import Visitor
from companies.models import Company
from datetime import date
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='accounts:login')
def index(request):
    visitors = Visitor.objects.filter(visit_date__gte=date.today())
    companies = Company.objects.all()
    context = {'visitors': visitors, 'companies': companies}
    return render(request, 'index.html', context)