# Generated by Django 5.0 on 2023-12-28 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpage', '0006_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
