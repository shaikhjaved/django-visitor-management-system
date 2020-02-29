from django.shortcuts import render, redirect
from .models import Visitor
from companies.models import Company
# from djangonautic.companies.models import Company
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.utils.timezone import datetime
from django.core.serializers.json import DjangoJSONEncoder
import json

# Create your views here.


def index(request):
    visitors = Visitor.objects.order_by('-visit_date')
    context = {'visitors': visitors}
    return render(request, 'visitors/index.html', context)


def onGetCreate(request):
    companies = Company.objects.all()
    context = {
        'companies': companies
    }
    return render(request, 'visitors/create.html', context)


def onPostCreate(request):
    response = {}
    if request.method == 'POST':
        visitor_phone = request.POST.get('visitor_phone')
        visitor_name = request.POST.get('visitor_name')
        visitor_from = request.POST.get('visitor_from')
        purpose_of_visit = request.POST.get('purpose_of_visit')
        company_id = request.POST.get('selectedcompanies')
        visitor_image = request.POST.get('visitor_image')

        visitor = Visitor(visitor_phone=visitor_phone,
                          visitor_name=visitor_name, visitor_from=visitor_from, purpose_of_visit=purpose_of_visit, company_id=company_id, visitor_image=visitor_image)
        visitor.save()
        response = {'status': True, 'visitor_id': visitor.pk}
    return JsonResponse(response)


def onPostDelete(request, id):
    if request.method == "GET":
        user = Visitor.objects.get(id=id)
        user.delete()
    return redirect('visitors:index')
