from django.contrib import admin

from discounts.models import Discount


class DiscountAdmin(admin.ModelAdmin):
    list_display = ['code', 'valid_to', 'discount', 'active']
    list_filter = ['active']
    search_fields = ['code']


admin.site.register(Discount, DiscountAdmin)
