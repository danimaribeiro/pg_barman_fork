# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('barman_home', models.CharField(max_length=300, verbose_name=u'Barman Location'),), ('barman_user', models.CharField(max_length=50, verbose_name=u'Barman User'),), ('log_file', models.CharField(max_length=300, verbose_name=u'Log file'),), ('compression', models.CharField(max_length=10, verbose_name=u'Compression', choices=((u'none', u'None',), (u'bzip2', u'bzip2',), (u'gzip', u'gzip',),)),), ('minimum_redundancy', models.IntegerField(verbose_name=u'Minimum Redundancy'),)],
            bases = (models.Model,),
            options = {u'ordering': ['barman_home', 'barman_user', 'minimum_redundancy'], u'verbose_name': u'Configuration', u'verbose_name_plural': u'Configurations'},
            name = 'BarmanConfiguration',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('unique_key', models.CharField(unique=True, max_length=50, verbose_name=u'Unique Key'),), ('description', models.CharField(max_length=100, verbose_name=u'Description'),), ('implementation_class_name', models.CharField(max_length=100, verbose_name=u'Class Name'),)],
            bases = (models.Model,),
            options = {},
            name = 'Storage',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('description', models.CharField(max_length=200, verbose_name=u'Description'),), ('last_backup', models.DateTimeField(null=True, verbose_name=u'Last Backup', blank=True),), ('backup_interval', models.TimeField(verbose_name=u'Backup Interval'),), ('configuration', models.ForeignKey(to=u'pg_barman.BarmanConfiguration', to_field=u'id'),)],
            bases = (models.Model,),
            options = {u'ordering': ['description', 'last_backup', 'backup_interval'], u'verbose_name': u'Backup Database', u'verbose_name_plural': u'Databases for backup'},
            name = 'BackupDatabase',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('description', models.CharField(max_length=100, verbose_name=u'Description'),), ('date_backup', models.DateTimeField(verbose_name=u'Backup Date'),), ('database_size', models.IntegerField(verbose_name=u'Database Size'),), ('file_size', models.IntegerField(verbose_name=u'File Size'),), ('database', models.ForeignKey(to=u'pg_barman.BackupDatabase', to_field=u'id'),)],
            bases = (models.Model,),
            options = {u'ordering': ['description', 'date_backup']},
            name = 'Backup',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('storage_key', models.CharField(max_length=100, verbose_name=u'Key'),), ('storage_value', models.CharField(max_length=500, verbose_name=u'Value'),), ('required', models.BooleanField(verbose_name=u'Required'),), ('storage', models.ForeignKey(to=u'pg_barman.Storage', to_field=u'id'),)],
            bases = (models.Model,),
            options = {},
            name = 'StorageConfiguration',
        ),
    ]
