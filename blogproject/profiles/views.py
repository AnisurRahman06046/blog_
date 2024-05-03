from django.shortcuts import render

# Create your views here.
def addProfile(request):
    return render(request,'add_profile.html')