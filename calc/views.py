from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    name = 'NBA Player Table'
    return render(request, 'home.html',{'name':name})

def add(request):
    if request.POST['math'] == 'add':
        val1 = int(request.POST['num1'])
        val2 = int(request.POST['num2'])
        res = val1 + val2
    if request.POST['math'] == 'subtract':
        val1 = int(request.POST['num1'])
        val2 = int(request.POST['num2'])
        res = val1 - val2
    if request.POST['math'] == 'multiply':
        val1 = int(request.POST['num1'])
        val2 = int(request.POST['num2'])
        res = val1 * val2
    if request.POST['math'] == 'divide':
        val1 = int(request.POST['num1'])
        val2 = int(request.POST['num2'])
        res = val1 / val2

    return render(request, "result.html", {"result": res})

def nba(request):
    Lebron = {'name':'LeBron James', 'team':'Los Angeles Lakers', 'Position': 'SF'}
    AD = {'name':'Anthony Davis', 'team':'Los Angeles Lakers', 'Position': 'PF'}
    Hero = {'name':'Tyler Herro', 'team':'Miami Heat', 'Position': 'SG'}
    players = [Lebron, AD, Hero]
    return render(request, 'nba.html', {'players': players})
