from urllib.parse import urlparse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404

from django.contrib import messages

from .models import Post

from .forms import PostForm
# Create your views here.

def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form =PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance =form.save(commit=False)
        instance.user= request.user
        instance.save()
        messages.success(request,"Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())

    context={
        "form" :form
    }
    return render(request,"post_form.html",context)



def post_detail(request,id):
    instance = get_object_or_404(Post,id=id)
    share_string = urlparse(instance.content)
    context = {
        "title" :instance.title,
        "instance" :instance,
        "share_string": share_string,
    }
    return render(request,"post_detail.html",context)

    

def post_list(request):
    queryset =Post.objects.all()
    context = {
        "object_list" :queryset
    }
    #return HttpResponse("<h1>Hello dere  lissssstttt!!!!!!!!!</h1>")
    return render(request, "index.html", context)  
    


def post_update(request,id):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post,id=id)
    form =PostForm(request.POST or None, request.FILES or None,instance=instance)
    if form.is_valid():
        instance =form.save(commit=False)
        instance.save()
        messages.success(request,"Changes Saved!!!!!")

        return HttpResponseRedirect(instance.get_absolute_url())
    context={
        "form" :form,
        "title":instance.title,
        "instance": instance
    }
    return render(request,"post_form.html",context)

    

def post_delete(request,id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post,id=id)
    instance.delete()
    messages.success(request,"Post Deleted!!!!!")
    return redirect("post:list")
    
    