# Generated by Django 4.2.2 on 2023-07-07 05:41

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webpage', '0003_delete_login'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='UserProfile',
        ),
    ]
