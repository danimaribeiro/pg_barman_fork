from django.db import models
from django.utils.translation import ugettext as _

class BarmanConfiguration(models.Model):
    description = models.CharField(_('Description'), max_length=50)
    barman_home = models.CharField(_('Barman Location'), max_length=300)
    barman_user = models.CharField(_('Barman User'), max_length=50)
    log_file = models.CharField(_('Log file'), max_length=300)
    COMPRESSION_CHOICES = (
        (u'none', u'None'),
        (u'bzip2', u'bzip2'),
        (u'gzip', u'gzip'),
    )
    compression = models.CharField(_('Compression'), choices=COMPRESSION_CHOICES, max_length=10)
    minimum_redundancy = models.IntegerField(_('Minimum Redundancy'))
    
    def __unicode__(self):
        return self.barman_home

    class Meta:
        ordering = ["barman_home", "barman_user", "minimum_redundancy"]
        verbose_name = _("Configuration")
        verbose_name_plural = _("Configurations")

      
class BackupDatabase(models.Model):
    description = models.CharField(_('Description'), max_length=200)    
    last_backup = models.DateTimeField(_('Last Backup'), null=True, blank=True)
    backup_interval = models.TimeField(_('Backup Interval'))
    configuration = models.ForeignKey(BarmanConfiguration, related_name=_('Configuration'))
    
    def __unicode__(self):
        return self.description
      
    class Meta:
        ordering = ["description", "last_backup", "backup_interval"]
        verbose_name = _("Backup Database")
        verbose_name_plural = _("Databases for backup")
        
class Backup(models.Model):
    description = models.CharField(_('Description'), max_length=100)
    name = models.CharField(_('Name'), max_length=100)
    date_backup = models.DateTimeField(_('Backup Date'))
    database_size = models.IntegerField(_('Database Size'))
    file_size = models.IntegerField(_('File Size'))
    file_location = models.CharField(_('File Location'), max_length=300)
    database = models.ForeignKey(BackupDatabase, related_name = _('Database'))
    
    def __unicode__(self):
        return self.description
      
    class Meta:
        ordering = [ "description", "date_backup" ]

class Storage(models.Model):
    """
    We can implement different types of Storage.    
    """    
    unique_key = models.CharField(_('Unique Key'), max_length=50, unique=True)
    description = models.CharField(_('Description'), max_length=100)
    implementation_class_name = models.CharField(_('Class Name'), max_length=100)
    
class StorageConfiguration(models.Model):
    storage_key = models.CharField(_('Key'), max_length=100)
    storage_value = models.CharField(_('Value'), max_length=500)
    required = models.BooleanField(_('Required'))
    storage = models.ForeignKey(Storage, related_name = _('Storage'))

    
