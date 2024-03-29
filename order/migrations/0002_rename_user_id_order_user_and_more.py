# Generated by Django 4.1.6 on 2023-02-28 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='orderdetail',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='orderdetail',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RemoveField(
            model_name='discountcode',
            name='expire_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='code_id',
        ),
        migrations.AddField(
            model_name='discountcode',
            name='code',
            field=models.CharField(default='code', max_length=10, unique=True),
        ),
        migrations.AddField(
            model_name='discountcode',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='discountcode',
            name='type',
            field=models.CharField(choices=[('P', 'Percent'), ('M', 'Money')], default='M', max_length=10),
        ),
        migrations.AddField(
            model_name='discountcode',
            name='valid_from',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='discountcode',
            name='valid_to',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='discount_code',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='order.discountcode'),
        ),
        migrations.AlterField(
            model_name='discountcode',
            name='value',
            field=models.IntegerField(),
        ),
    ]
