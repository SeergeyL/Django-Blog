# Generated by Django 3.1.7 on 2021-04-14 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210414_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='avatars/avatar.jpg', upload_to='avatars/'),
        ),
    ]
