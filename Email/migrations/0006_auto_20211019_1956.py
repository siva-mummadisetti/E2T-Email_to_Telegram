# Generated by Django 3.2.2 on 2021-10-19 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Email', '0005_auto_20211019_1157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email_password',
            new_name='emailPassword',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='telegram_id',
            new_name='telegramId',
        ),
    ]
