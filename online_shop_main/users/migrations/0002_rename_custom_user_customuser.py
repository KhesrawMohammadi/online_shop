# Generated by Django 5.1.6 on 2025-02-27 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Custom_user',
            new_name='CustomUser',
        ),
    ]
