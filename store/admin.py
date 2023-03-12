

from django.contrib import admin

from store.models import Retail, Supplier, Product, Contact


class LinkAdmin(admin.ModelAdmin):

    list_display = ('title', 'contact', 'product', 'supplier', 'debt', 'created')
    list_display_links = ('title', 'supplier',)
    list_filter = ('contact__city',)
    search_fields = ('contact__city',)

    def clear_receivables(self, request, queryset):
        queryset.update(receivables=0)

    actions = [clear_receivables]


admin.site.register(Retail, LinkAdmin)
admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Contact)