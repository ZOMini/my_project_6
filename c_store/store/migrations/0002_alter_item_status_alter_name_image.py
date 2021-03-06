# Generated by Django 4.0.4 on 2022-07-17 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.CharField(choices=[('Warehouse', 'Warehouse'), ('Store', 'Store'), ('In_magaz', 'From warehouse in store'), ('Order', 'Order and wait proccesing'), ('Wait', 'Wait purchase'), ('Sold', 'Sold in magazine')], default='Store', max_length=32, verbose_name='Место нахожднения/Статус'),
        ),
        migrations.AlterField(
            model_name='name',
            name='image',
            field=models.ImageField(blank=True, upload_to='store/', verbose_name='Картинка'),
        ),
    ]
