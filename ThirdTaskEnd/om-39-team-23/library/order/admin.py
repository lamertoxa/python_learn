from django.contrib import admin


from .models import Order

admin.site.register(Order)


class OrderAdmin(admin.ModelAdmin):

    list_display = ('id','user','book','created_at','end_at','plated_end_at')
    fields = ('user','book',('end_at','plated_end_at'))
admin.site.unregister(Order)
admin.site.register(Order,OrderAdmin)
