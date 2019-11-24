# Generated by Django 2.2.7 on 2019-11-22 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='district',
            name='id',
        ),
        migrations.RemoveField(
            model_name='rep',
            name='id',
        ),
        migrations.RemoveField(
            model_name='zip',
            name='id',
        ),
        migrations.AlterField(
            model_name='district',
            name='zcta',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rep',
            name='zip',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='zip',
            name='zip',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]