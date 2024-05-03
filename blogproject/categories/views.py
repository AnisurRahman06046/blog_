from django.shortcuts import render,redirect
from categories.forms import CategoryForm

# Create your views here.
def addCategory(request):
    if request.method=='POST':
        category = CategoryForm(request.POST)
        if category.is_valid():
            category.save()
            return redirect('addCategory')
    else:
        category = CategoryForm()
    return render(request,'add_categories.html',{'form':category})