# Generated by Django 4.1.6 on 2023-02-14 09:08

from django.db import migrations
import django.db.models.deletion
import iranian_cities.fields


class Migration(migrations.Migration):

    dependencies = [
        ('iranian_cities', '0004_remove_abadi_shhahr'),
        ('accounts', '0002_alter_address_province'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=iranian_cities.fields.ShahrestanField(on_delete=django.db.models.deletion.CASCADE, to='iranian_cities.shahrestan'),
        ),
    ]
