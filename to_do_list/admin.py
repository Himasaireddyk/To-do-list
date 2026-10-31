from django.contrib import admin

# Register your models here.
from .models import task
# Register your models here.
class tasAdmin(admin.ModelAdmin):
         list_display=('task','is_completed',)
         search_fields=('task',)
admin.site.register(task,tasAdmin)