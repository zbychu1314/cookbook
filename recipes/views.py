from django.shortcuts import render
from .models import Recipe

# Create your views here.
def list(request):
    
    if request.method == "GET":
        r = Recipe.objects.all()

   

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
        "recipes/list.html",
        {"recipes": r}
    )
  