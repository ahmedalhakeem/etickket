# Generated by Django 3.1.3 on 2021-02-03 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eticket', '0003_remove_section_dept'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_type', models.CharField(choices=[('SW', 'software'), ('HW', 'hardware')], default='SW', max_length=2)),
                ('ticket_status', models.CharField(choices=[('مهمة جدا', 'high_priority'), ('مهمة', 'normal_priority'), ('متوسطة الاهمية', 'low_priority')], default='مهمة جدا', max_length=14)),
                ('title', models.CharField(blank=True, max_length=30, null=True)),
                ('description', models.TextField(blank=True, max_length=100, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
                ('it_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='it_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Problems',
        ),
        migrations.DeleteModel(
            name='ProblemType',
        ),
    ]
