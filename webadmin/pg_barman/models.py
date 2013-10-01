from django.db import models
from django.utils.translation import ugettext as _

class BarmanConfiguration(models.Model):
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

      
class backup_database(models.Model):
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
