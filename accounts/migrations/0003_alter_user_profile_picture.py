# Generated by Django 3.2.3 on 2021-07-12 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210712_0559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, default='defaults/uknown_profile_picture.jpeg', null=True, upload_to='user_profile_pics'),
        ),
    ]