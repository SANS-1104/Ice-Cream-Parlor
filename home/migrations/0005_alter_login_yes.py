# Generated by Django 5.0.3 on 2024-03-27 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_mobile_login_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='yes',
            field=models.BooleanField(verbose_name=models.NullBooleanField(verbose_name=True)),
        ),
    ]
