# Generated by Django 4.0.3 on 2022-07-22 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_uploadimage_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UploadImage',
            new_name='UploadImageAchieve',
        ),
    ]
