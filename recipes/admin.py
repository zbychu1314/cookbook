from django.contrib import admin
from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display =["id","title","short_description"]

    def short_description(self,obj):
        return obj.description[:10] + "..."
    
    def get_list_display(self,request):

        '''
        sterowanie wyswietlaniem dla konkretnej osoby, np dla super admin
        '''

        if request.user.is_superuser is False:
            return ["title"]
        return self.list_display


