# Generated by Django 4.2 on 2023-12-21 11:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0002_alter_trainstation_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='train',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
