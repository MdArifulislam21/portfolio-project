# Generated by Django 2.0 on 2020-02-19 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_auto_20200219_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='images/'),
        ),
    ]
