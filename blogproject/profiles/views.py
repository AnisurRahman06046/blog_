from django.shortcuts import render,redirect
from profiles.forms import ProfileForm


# Create your views here.
def addProfile(request):
    if request.method=='POST':
        author_profile = ProfileForm(request.POST)
        if author_profile.is_valid():
            author_profile.save()
            return redirect('addProfile')
    else:
        author_profile= ProfileForm()
    return render(request,'add_profile.html',{'form':author_profile})