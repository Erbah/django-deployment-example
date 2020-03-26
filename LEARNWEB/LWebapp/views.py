from django.shortcuts import render

# Create your views here.

home_dict = ''

def homeView(request):
    context_dict = {'home_dict': home_dict}
    return render(request,'LWebapp/home.html',context_dict,)

# class homeView(request):
#     context_dict = {'home_dict': home_dict}
#     return render(request,'LWebapp/home.html'context_dict)
