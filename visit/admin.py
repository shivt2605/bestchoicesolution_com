from django.contrib import admin

# Register your models here.

from visit.models import *


class Meeting_TabularInline(admin.TabularInline):
    model = Meeting


class Image_TabularInline(admin.TabularInline):
    model = Image




class visit_admin(admin.ModelAdmin):
    list_display = ['id','visit_for','industry','form_name','full_address','locality','visit_response', 'contact_person','number','email_id','featured_image','map_link','comment','created_at','call_status']
    list_filter = ('visit_for','industry','locality','visit_response','call_status' )
    list_editable = ( 'visit_response','comment','call_status')
    search_fields = ('id', 'contact_person', 'number','form_name',)
    list_per_page = 25
    inlines = (Meeting_TabularInline,Image_TabularInline)




class meeting_admin(admin.ModelAdmin):
    list_display = ('visit','date','comment')
    list_filter = ['date']
    list_editable = ['date','comment']
    list_per_page = 25




admin.site.register(Meeting,meeting_admin)
admin.site.register(Call_Status)
admin.site.register(Visit,visit_admin)
admin.site.register(Image,)

admin.site.register(Industry)
admin.site.register(City)
admin.site.register(Locality)
admin.site.register(Visit_Response)