from django.shortcuts import render, redirect

# Create your views here.

from django.shortcuts import render
from .models import Post
from django.http import Http404

# Create your views here.
def list(request):
    
    if request.method == "GET":
        p = Post.objects.all()

   

    #if request.method == "POST":
    #    service.create(title=request.POST.get("pos_title"),
    #                   content=request.POST.get("pos_content"),
    #                   created_at=request.POST.get("pos_created_at"),
    #                   updated_at=request.POST.get("pos_updated_at")
    #                   )
        #p = Post.objects.create(
        #    title=request.POST.get("pos_title"),
        #    content=request.POST.get("pos_content"),
        #    created_at=request.POST.get("pos_created_at"),
        #    updated_at=request.POST.get("pos_updated_at")
        # )  # date="2022...", systolic=120
        #
        #p = Post.objects.all()
    #    p = service.list()
    
    return render(
        request, 
        "posts/list.html",
        {"posts": p}
    )

def details(request, id):
    
    #p = Post.objects.get(id=id)

    try:
        p = Post.objects.get(id=id)
    except:
        raise Http404

    return render(
        request, 
        "posts/details.html",
        {"posts": p}
    )

def create(request):
    p = Post.objects.create(
            title=request.POST.get("pos_title"),
            description=request.POST.get("pos_description"),
            created_at=request.POST.get("pos_category"),
            updated_at=request.POST.get("pos_author")
         ) 
    return redirect("/posts/")
