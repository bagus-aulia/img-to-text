# Generated by Django 2.2.4 on 2019-10-20 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='attachment',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
