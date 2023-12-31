# Generated by Django 5.0 on 2023-12-15 06:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrainStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('No', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=255)),
                ('address', models.TextField(max_length=500)),
                ('phone_number', models.CharField(max_length=12)),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=10, verbose_name='code')),
                ('capacity', models.IntegerField()),
                ('price', models.FloatField(help_text='price in Rial')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train.trainstation')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin', to='train.trainstation')),
            ],
        ),
    ]
