from django.shortcuts import render, redirect  
from BLOG.forms import BLOGForm  
from BLOG.models import BLOG  
  
def emp(request):  
    if request.method == "POST":  
        form = BLOG.Form(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = BLOGForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    BLOG = BLOG.objects.all()  
    return render(request,"show.html",{'BLOG':BLOG})  
def edit(request, id):  
    BLOG = BLOG.objects.get(id=id)  
    return render(request,'edit.html', {'BLOG':BLOG})  
def update(request, id):  
    BLOG = BLOG.objects.get(id=id)  
    form = BLOGForm(request.POST, instance = BLOG)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'BLOG': BLOG})  
def destroy(request, id):  
    BLOG = BLOG.objects.get(id=id)  
    BLOG.delete()  
    return redirect("/show")  
