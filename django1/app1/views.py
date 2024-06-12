from django.shortcuts import render
from django.http import HttpResponse
from app1.forms import inputform1

# Create your views here.
def square(request):
    num=2
    sq=num*num
    return render(request,'index1.html',{'p1':sq,'p2':num})
def home(request):
    n=5
    fact1=1
    for i in range(1,n+1,1):
        fact1=fact1*i
    return render(request,'index.html',{'param1':fact1,'param2':n})
def fact2(request):
  
    fact_list = []
    for num in range(3, 9):
        fact = 1
        for i in range(1, num + 1):
            fact = fact * i
        fact_list.append((num, fact))
    return render(request, 'index3.html', {'fact_list': fact_list})
def factorial_input(request):
    if request.method == 'POST':
        num = int(request.POST.get('num'))
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        return HttpResponse(f"The factorial of {num} is {fact}")
    return render(request, 'index4.html')
def get_possibilities(s):
    if len(s) == 1:
        return [s]
    possibilities = []
    for i in range(len(s)):
        char = s[i]
        remaining_str = s[:i] + s[i+1:]
        for p in get_possibilities(remaining_str):
            possibilities.append(char + p)
    return possibilities

def index(request):
    if request.method == 'POST':
        input_string = request.POST.get('input_string')
        permutations = get_possibilities(input_string)
        return render(request, 'sub.html', {'permutations': permutations, 'input_string': input_string})
    return render(request, 'sub.html')


def home1(request):
    if request.method=="POST":
       form1=inputform1(request.POST)
       if form1.is_valid():
             data=form1.cleaned_data['n']
             result=factorial(data)

             return render(request,'ii.html',{'form':form1,'par':result})
    else:
         form1=inputform1()
         return render(request,'ii.html',{'form':form1})


def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f