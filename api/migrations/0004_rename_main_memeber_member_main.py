# Generated by Django 5.0.2 on 2024-07-03 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_member_main_memeber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='main_memeber',
            new_name='main',
        ),
    ]