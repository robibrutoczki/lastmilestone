# Generated by Django 3.0.6 on 2020-10-01 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20200927_1428'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='original_basket',
            new_name='original_bag',
        ),
    ]
