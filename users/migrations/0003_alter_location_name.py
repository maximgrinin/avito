# Generated by Django 4.1.5 on 2023-01-27 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_birth_date_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
