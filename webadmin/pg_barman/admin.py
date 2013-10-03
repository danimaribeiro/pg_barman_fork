#coding=utf-8
from models import BackupDatabase, BarmanConfiguration, Storage, StorageConfiguration, Backup
from django.contrib import admin
from actions import export_as_csv, schedule_full_backup   

class BackupDatabaseAdmin(admin.ModelAdmin):
    fields = ['description', 'backup_interval', 'configuration', 'last_backup']
    list_display  = ['description', 'last_backup', 'backup_interval']
    search_fields = ['description','last_backup']
    list_filter = ['last_backup']
    actions = [export_as_csv]
    readonly_fields = ['last_backup']

class BarmanConfigurationAdmin(admin.ModelAdmin):
    fields = ['description','barman_home', 'barman_user', 'log_file', 'compression', 'minimum_redundancy']
    list_display  = ['description', 'compression', 'minimum_redundancy']
    actions = [export_as_csv]
    
class StorageConfigurationAdmin(admin.TabularInline):
    model = StorageConfiguration
    max_num = 1
    fields = ['storage_key', 'storage_value']

class StorageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return True
    def has_change_permission(self, request, obj=None):
        return True
    def has_delete_permission(self, request, obj=None):
        return False
    inlines = [StorageConfigurationAdmin]
  

class BackupAdmin(admin.ModelAdmin):
    fields = ['description','name', 'date_backup']
    actions = [schedule_full_backup]

#admin.site.disable_action('delete_selected')
admin.site.register(Storage, StorageAdmin)
admin.site.register(BarmanConfiguration, BarmanConfigurationAdmin)
admin.site.register(BackupDatabase, BackupDatabaseAdmin)
admin.site.register(Backup, BackupAdmin)



