# Generated by Django 4.2 on 2023-11-23 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_remove_stock_date_added_stock_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='amount',
            new_name='total_amount',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='date_sold',
        ),
    ]
