from django.contrib import admin
from .models import Registration, District, Branch





class Register_FormAdmin(admin.ModelAdmin):
    list_display = ('Name', 'dob', 'age', 'Gender', 'phone_number', 'email_id', 'district', 'branch', 'account_type', 'materials_provide')

admin.site.register(Registration, Register_FormAdmin)



class District_ForAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(District, District_ForAdmin)


class Branch_ForAdmin(admin.ModelAdmin):
    list_display = ('district', 'name')
admin.site.register(Branch, Branch_ForAdmin)
