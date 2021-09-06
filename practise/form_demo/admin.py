from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Customer

admin.site.site_header = "Admin Dashboard"

class CustomerAdmin(admin.ModelAdmin):
    # show select filed as colum 
    list_display = ('id','first_name','last_name','email','created_date')
    list_display_links = ('id','first_name')
    list_editable= ('email',)
    search_fields= ('first_name','last_name','email')

    # add filter
    list_filter  = ('created_date',)



# Register your models here.

admin.site.register(Customer,CustomerAdmin)
admin.site.unregister(Group)