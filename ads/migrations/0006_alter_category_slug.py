# Generated by Django 4.1.5 on 2023-01-27 15:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0005_category_slug_alter_ad_description_alter_ad_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]
