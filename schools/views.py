from django.contrib.auth.decorators import login_required
import schools
from schools.models import Schools
from django.shortcuts import render, redirect
from django.db import models
from bs4 import BeautifulSoup
import requests

# Create your views here.
def front(request):
    return render(request, 'front.html', {'message':'Welcome to LanguageScrape'})


@login_required
def list(request):
    schools_list = Schools.objects.all()
    return render(request, 'list.html', {'schools_list':schools_list})

def index(request):
    schools_list = Schools.objects.all()
    return render(request, 'index.html', {'schools_list':schools_list})

@login_required
def detail(request, pk):
    school = Schools.objects.get(pk=pk)
    return render(request, 'detail.html', {'school':school})

def detail2(request, pk):
    school = Schools.objects.get(pk=pk)
    return render(request, 'detail2.html', {'school':school})

@login_required
def create(request):
    if request.method == 'POST':
        school = Schools(name=request.POST.get('name'), content=request.POST.get('content'), 
        category=request.POST.get('category'), price=request.POST.get('price'))
        school.save()
        return redirect('list')
    else:
        return render(request, 'create.html')

@login_required        
def scrape(request):
    url = 'https://www.icls.com.my/'
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')

    datas = []
    all_h3 = soup.select('div.box-text-inner h3 a')
    for h3 in all_h3:
        data = h3.get_text(strip=True)
        datas.append(data)
    latestdatas = set(datas)
        

    if request.method == 'POST':    
        school = Schools(name=request.POST.get('name'), 
        content=request.POST.get('content'), category=request.POST.get('category'), price=request.POST.get('price'))
        school.save()
        return redirect('list')
    else:
        return render(request, 'scrape.html', {'data': latestdatas})

@login_required
def update(request, pk):
    school = Schools.objects.get(pk=pk)
    if request.method == 'POST':
            school.name = request.POST.get('name')
            school.content = request.POST.get('content')
            school.category = request.POST.get('category')
            school.price = request.POST.get('price')             
            school.save()
            return redirect('list')
    else:
            return render(request, 'update.html', {'school': school})

@login_required
def delete(request, pk):
    school = Schools.objects.get(pk=pk)
    if request.method == 'POST':
        school.delete()
        return redirect('list')
    return render(request, 'delete.html', {'school': school})