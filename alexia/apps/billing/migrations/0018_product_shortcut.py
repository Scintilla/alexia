# Generated by Django 2.2.24 on 2021-08-16 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0017_auto_20210326_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='shortcut',
            field=models.CharField(blank=True, max_length=1, verbose_name='shortcut'),
        ),
    ]
