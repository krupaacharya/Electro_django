# Generated by Django 4.0.6 on 2022-08-09 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='', upload_to='profile_pic/'),
            preserve_default=False,
        ),
    ]
