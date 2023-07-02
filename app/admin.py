from django.contrib import admin

from .models import *

# Register your models here.

class Fqa_TabularInline(admin.TabularInline):
    model = Fqa

class Feature_TabularInline(admin.TabularInline):
    model = Feature


class service_admin(admin.ModelAdmin):
    inlines = (Fqa_TabularInline,Feature_TabularInline)



admin.site.register(Categories)
admin.site.register(Plat_Form)
admin.site.register(Service,service_admin)
admin.site.register(Fqa)
admin.site.register(Feature)
admin.site.register(UserService)
admin.site.register(Payment)