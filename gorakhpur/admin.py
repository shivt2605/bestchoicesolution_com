from django.contrib import admin

# Register your models here.

from gorakhpur.models import *


class Interested_TabularInline(admin.TabularInline):
    model = Interested


class For_Job_TabularInline(admin.TabularInline):
    model = For_Job



class For_Coaching_TabularInline(admin.TabularInline):
    model = For_Coaching


class response_admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'number', 'status', 'created_at', 'comment','call_status' )
    list_filter = ('status', 'created_at', 'call_status' )
    list_editable = ( 'name', 'number','status','call_status')
    search_fields = ('id', 'name', 'number',)
    list_per_page = 25
    inlines = (Interested_TabularInline,For_Coaching_TabularInline)


class Interested_admin(admin.ModelAdmin):
    list_display = ('id','response','interested_type','comment','follow_up','call_status')
    list_filter = ('response','interested_type','follow_up','call_status' )
    list_editable = ( 'interested_type','comment','follow_up','call_status')
    search_fields = ('id', 'name', 'number',)
    list_per_page = 25

admin.site.register(Status)
admin.site.register(Call_Status)
admin.site.register(Response,response_admin)
admin.site.register(Interested,Interested_admin)

admin.site.register(For_Job)
admin.site.register(For_Coaching)