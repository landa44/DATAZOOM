# Generated by Django 4.0 on 2022-01-26 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('blog', '0005_interest_created_interest_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interest',
            name='users',
        ),
        migrations.AddField(
            model_name='interest',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='interests', to='auth.user'),
            preserve_default=False,
        ),
    ]
