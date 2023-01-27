# Generated by Django 4.1.5 on 2023-01-27 15:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_selection'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='name',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.AlterField(
            model_name='ad',
            name='price',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]