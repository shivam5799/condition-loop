from django.shortcuts import render

# Create your views here.



def conditions(request):
    d={'a':19,'b':20,'c':200}
    return render(request,'conditions.html',context=d)


def loop(request):
     d={'name':'AKASH'}
     return render(request,loop,loop.html,context=d)