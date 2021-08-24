import schools
from schools.models import Schools
from django.shortcuts import render, redirect

# Create your views here.
def main(request):
    return render(request, 'main.html', {'message':'Welcome to LanguageScrape'})

def list(request):
    schools_list = Schools.objects.all()
    return render(request, 'list.html', {'schools_list':schools_list})

def detail(request, pk):
    school = Schools.objects.get(pk=pk)
    return render(request, 'detail.html', {'school':school})

def create(request):
    if request.method == 'POST':
        school = Schools(name=request.POST.get('name'), content=request.POST.get('content'), category=request.POST.get('category'))
        school.save()
        return redirect('list')
    else:
        return render(request, 'create.html')

def update(request, pk):
    school = Schools.objects.get(pk=pk)
    if request.method == 'POST':
            school.name = request.POST.get('name')
            school.content = request.POST.get('content')
            school.category = request.POST.get('category')            
            school.save()
            return redirect('list')
    else:
            return render(request, 'update.html', {'school': school})

def delete(request, pk):
    school = Schools.objects.get(pk=pk)
    if request.method == 'POST':
        school.delete()
        return redirect('list')
    return render(request, 'delete.html', {'school': school})