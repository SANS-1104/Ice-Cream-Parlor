# Generated by Django 5.0.3 on 2024-03-27 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_login_mobile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='mobile',
            new_name='phone',
        ),
    ]
