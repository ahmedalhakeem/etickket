# Generated by Django 3.1.3 on 2021-02-03 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eticket', '0004_auto_20210203_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='it_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='it_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
