from models import BackupDatabase, BarmanConfiguration
from django.contrib import admin
from actions import export_as_csv    

class BackupDatabaseAdmin(admin.ModelAdmin):
    fields = ['description', 'backup_interval', 'configuration', 'last_backup']
    list_display  = ['description', 'last_backup', 'backup_interval']
    search_fields = ['description','last_backup']
    list_filter = ['last_backup']
    actions = [export_as_csv]
    readonly_fields = ['last_backup']

class BarmanConfigurationAdmin(admin.ModelAdmin):
    actions = [export_as_csv]
    
#admin.site.disable_action('delete_selected')
admin.site.register(BarmanConfiguration, BarmanConfigurationAdmin)
admin.site.register(BackupDatabase, BackupDatabaseAdmin)