# Generated by Django 3.2.19 on 2023-07-08 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20230707_1810'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='user',
        ),
    ]
