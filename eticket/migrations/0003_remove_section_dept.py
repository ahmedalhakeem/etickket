# Generated by Django 3.1.3 on 2021-01-25 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eticket', '0002_auto_20210120_1256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='dept',
        ),
    ]