# Generated by Django 4.1.6 on 2023-02-03 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('alley', models.CharField(max_length=50)),
                ('num', models.CharField(max_length=5)),
                ('postal_code', models.CharField(max_length=10)),
            ],
        ),
    ]
