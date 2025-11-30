from django.shortcuts import render,redirect,get_object_or_404
from .models import blogmodel
from .forms import blogform


from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator


from django.contrib.auth.decorators import login_required
# Create your views here.

@never_cache
@login_required
def home(request):
    posts = blogmodel.objects.exclude(Author = request.user)
    return render(request,'home.html',{'posts':posts})


@never_cache
@login_required
def myblogs(request):
    post = blogmodel.objects.filter(Author = request.user)
    return render(request,'myblogs.html',{'post':post})


@never_cache
@login_required
def create(request):
    form = blogform()
    if request.method == 'POST':
        form = blogform(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.Author = request.user
            new.save()
            return redirect('home')
    return render(request,'create.html',{'form':form})


@never_cache
@login_required
def update(request,pk):
    post = get_object_or_404(blogmodel,pk = pk)
    form = blogform(instance=post)
    
    if request.method == 'POST':
        form = blogform(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    return render(request,'update.html',{'form':form})

@never_cache
@login_required
def delete(request,pk):
    post = get_object_or_404(blogmodel,pk = pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request,'delete.html',{'post':post})



