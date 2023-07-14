from django.contrib import admin


from .models import CustomUser

admin.site.register(CustomUser)


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','middle_name','last_name','email','created_at','updated_at','role','is_superuser')
admin.site.unregister(CustomUser)
admin.site.register(CustomUser,CustomUserAdmin)
