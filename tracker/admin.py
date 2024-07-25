from django.contrib import admin
from .models import Crypto,Price

class CryptoAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol',)
    list_filter = ('symbol',)
    search_fields = ('name', 'symbol',)

class PriceAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'price',"created_at")
    list_filter = ('symbol',)
    search_fields = ('symbol__symbol',)

admin.site.register(Crypto,CryptoAdmin)
admin.site.register(Price,PriceAdmin)