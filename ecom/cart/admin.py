from django.contrib import admin
from .models import cart
# Register your models here.
class cartAdmin(admin.ModelAdmin):
    model=cart
    list_display=('item','user','quantity','is_active')


admin.site.register(cart,cartAdmin)