# Generated by Django 4.1.7 on 2023-03-19 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_upload_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='desc',
            field=models.TextField(max_length=500),
        ),
    ]
