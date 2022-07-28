from django.contrib import admin
from .models import Card


class CardAdmin(admin.ModelAdmin):
    model = Card
    list_display = ('title', 'category', 'author', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('category',)


admin.site.register(Card, CardAdmin)
