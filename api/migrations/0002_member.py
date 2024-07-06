# Generated by Django 5.0.2 on 2024-07-03 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('job', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='member/')),
            ],
        ),
    ]
