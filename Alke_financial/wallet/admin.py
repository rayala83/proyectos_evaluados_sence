from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Currency, User, Transaction, Contact

admin.site.register(User, UserAdmin)

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('currency_name', 'currency_symbol')

@admin.register(Transaction)
class TransactioAdmin(admin.ModelAdmin):
    list_display = ('sender','receiver','amount','transaction_date')
    search_fields =  ('transaction_date',)


@admin.register(Contact)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('owner','name','email')
    search_fields =  ('email',)