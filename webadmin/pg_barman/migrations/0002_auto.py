# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [('pg_barman', '0001_initial')]

    operations = [
        migrations.AddField(
            field = models.CharField(default='blank', max_length=50, verbose_name=u'Description'),
            name = 'description',
            model_name = 'barmanconfiguration',
        ),
        migrations.AddField(
            field = models.CharField(default='', max_length=300, verbose_name=u'File Location'),
            name = 'file_location',
            model_name = 'backup',
        ),
        migrations.AddField(
            field = models.CharField(default='', max_length=100, verbose_name=u'Name'),
            name = 'name',
            model_name = 'backup',
        ),
    ]
