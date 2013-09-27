from django.db import models
from django.utils.translation import ugettext as _

class backup_database(models.Model):
    description = models.CharField(_('Description'), max_length=200)    
    last_backup = models.DateTimeField(_('Last Backup'), null=True, blank=True)
    backup_interval = models.TimeField(_('Backup Interval'))
    
    def __unicode__(self):
        return self.description
      
    class Meta:
        ordering = ["description", "last_backup", "backup_interval"]
        verbose_name = _("Backup Database")
        verbose_name_plural = _("Databases for backup")
