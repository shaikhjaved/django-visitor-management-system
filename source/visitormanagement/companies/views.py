from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from .models import Company
# Create your views here.


def index(request):
    companies = Company.objects.all()
    context = {'companies': companies}
    return render(request, 'companies/index.html', context)


def onGetCreate(request):
    return render(request, 'companies/create.html')


def onPostCreate(request):
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        company_phone = request.POST.get('company_phone')
        company_email = request.POST.get('company_email')
        company_owner = request.POST.get('company_owner')
        contact_person = request.POST.get('contact_person')
        company_address = request.POST.get('company_address')

        company = Company(company_name=company_name, company_phone=company_phone, company_email=company_email,
                          company_owner=company_owner, contact_person=contact_person, company_address=company_address)
        company.save()
    return redirect('companies:index')


def onGetEdit(request, id):
    companies = Company.objects.get(id=id)
    context = {'companies': companies}
    return render(request, 'companies/edit.html', context)


def onPostEdit(request, id):
    if request.method == "POST":
        company_name = request.POST.get('company_name')
        company_phone = request.POST.get('company_phone')
        company_email = request.POST.get('company_email')
        company_owner = request.POST.get('company_owner')
        contact_person = request.POST.get('contact_person')
        company_address = request.POST.get('company_address')
        Company.objects.filter(id=id).update(company_name=company_name, company_phone=company_phone, company_email=company_email,
                                             company_owner=company_owner, contact_person=contact_person, company_address=company_address)
    return redirect('companies:index')


def onPostDelete(request, id):
    if request.method == "GET":
        user = Company.objects.get(id=id)
        user.delete()
    return redirect('companies:index')
