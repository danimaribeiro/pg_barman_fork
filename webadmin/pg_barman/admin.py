from models import backup_database
from django.contrib import admin

class BackupDatabaseAdmin(admin.ModelAdmin):
    fields = ['description', 'last_backup', 'backup_interval']
    list_display  = ['description', 'last_backup', 'backup_interval']
    search_fields = ['description','last_backup']
    list_filter = ['last_backup']

admin.site.register(backup_database, BackupDatabaseAdmin)