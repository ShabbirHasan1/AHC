# Generated by Django 4.0.4 on 2022-05-07 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahc_app', '0004_user_super_client_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mobile_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
