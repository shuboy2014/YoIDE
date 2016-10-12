from django.contrib import admin
from models import Hits


# Register your models here.

class HitsAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'hits']

    class Meta:
        model = Hits


admin.site.register(Hits, HitsAdmin)
