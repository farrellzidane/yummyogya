# Generated by Django 5.1.2 on 2024-10-19 05:02

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makanan',
            name='harga',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='makanan',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
