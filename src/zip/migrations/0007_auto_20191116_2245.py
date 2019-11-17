# Generated by Django 2.2.7 on 2019-11-17 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zip', '0006_auto_20191116_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='district',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('congressional_district', models.IntegerField(default=0)),
                ('zcta', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameField(
            model_name='zip',
            old_name='congressional_district',
            new_name='zip',
        ),
        migrations.RemoveField(
            model_name='zip',
            name='zcta',
        ),
        migrations.AddField(
            model_name='rep',
            name='zip',
            field=models.IntegerField(default=0),
        ),
    ]
