# Generated by Django 2.2.7 on 2019-11-20 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
        migrations.CreateModel(
            name='rep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip', models.IntegerField(default=0)),
                ('f_name', models.TextField()),
                ('l_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='zip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip', models.IntegerField(default=0)),
                ('county', models.TextField(default='')),
            ],
        ),
    ]
