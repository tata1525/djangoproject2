from django.contrib import admin
from .models import Advertisement

# Register your models here.
class AdvertisementAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'description', 'price', 'auction', 'create_at', 'image' ]
    list_filter=['auction', 'create_at']
    actions=['make_auction_as_false', 'make_auction_as_true']
    fieldsets=(
        ('Общее', {
            'fields': ('title', 'description', 'image'),
         }),
         ('Финансы', {
             'fields':('price','auction'),
             'classes':['collapse'],   
         })

    )

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):  #qertyset у лектора
        queryset.update(action=False)     

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):  #qertyset
        queryset.update(action=True)    



admin.site.register(Advertisement, AdvertisementAdmin)