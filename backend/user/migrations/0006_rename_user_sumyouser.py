# Generated by Django 4.0.6 on 2023-07-24 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('like', '0004_alter_like_user'),
        ('admin', '0006_alter_logentry_user'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('refrigerator', '0004_alter_refrigerator_user'),
        ('user', '0005_delete_sumyouser_user_groups_user_user_permissions'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='SumyoUser',
        ),
    ]
