# Generated by Django 4.1.6 on 2023-02-28 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, choices=[('BK', 'Black'), ('WT', 'White'), ('RD', 'Red'), ('BU', 'Blue'), ('GR', 'Green')], max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(blank=True, choices=[('XS', 'Xsmall'), ('S ', 'Small'), ('M ', 'Medium'), ('L ', 'Large'), ('XL', 'Xlarge')], max_length=2, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.AddField(
            model_name='product',
            name='colors',
            field=models.ManyToManyField(to='product.color'),
        ),
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.ManyToManyField(to='product.size'),
        ),
    ]