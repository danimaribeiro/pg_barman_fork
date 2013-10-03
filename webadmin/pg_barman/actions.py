import csv
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.utils.translation import ugettext as _

def export_as_csv(modeladmin, request, queryset):
    """
    Generic csv export admin action.
    """
    if not request.user.is_staff:
        raise PermissionDenied
    opts = modeladmin.model._meta
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s.csv' % unicode(opts).replace('.', '_')
    writer = csv.writer(response,delimiter=';')
    field_names = [field.name for field in opts.fields]
    # Write a first row with header information
    writer.writerow(field_names)
    # Write data rows
    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in field_names])
    return response
export_as_csv.short_description = _("Export selected objects as csv file")


def schedule_full_backup(modeladmin, request, queryset):
    """
    Schedule a full backup for the database
    """
    pass

schedule_full_backup.short_description = _("Schedule a full backup")

def schedule_incremental_backup(modeladmin, request, queryset):
    """
    Schedule a partial backup
    """
    pass
  
