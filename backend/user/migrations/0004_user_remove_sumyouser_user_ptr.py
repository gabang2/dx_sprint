# Generated by Django 4.0.6 on 2023-07-24 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_user_sumyouser'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_number', models.TextField(max_length=30, unique=True)),
                ('registered_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자',
                'db_table': 'sumyo_user',
            },
        ),
        migrations.RemoveField(
            model_name='sumyouser',
            name='user_ptr',
        ),
    ]
