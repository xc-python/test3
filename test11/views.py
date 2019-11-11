from django.shortcuts import render ,HttpResponse

# Create your views here.



def run(request):
    print(6666)
    return HttpResponse('hello world!')

