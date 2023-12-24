# Generated by Django 4.2 on 2023-12-23 09:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('FUEL', 'Fuel'), ('FISH', 'Fish'), ('FRY', 'Fry')], default=1, max_length=50)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('status', models.CharField(choices=[('1', 'Active'), ('0', 'Inactive')], default=1, max_length=2)),
                ('price', models.FloatField(default=0, max_length=(15, 2))),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_products', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='sale',
            options={'verbose_name_plural': 'Sales'},
        ),
        migrations.AlterModelOptions(
            name='stock',
            options={'verbose_name_plural': 'Stocks'},
        ),
        migrations.RemoveField(
            model_name='sale',
            name='fuel',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='fuel',
        ),
        migrations.DeleteModel(
            name='Fuel',
        ),
        migrations.AddField(
            model_name='sale',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='management.product'),
        ),
        migrations.AddField(
            model_name='stock',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='management.product'),
        ),
        migrations.AddField(
            model_name='stock',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='unit_stocks', to='management.unit'),
        ),
    ]
