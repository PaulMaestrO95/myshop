# Generated by Django 4.2.1 on 2023-05-08 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_index_together'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='product',
            index_together={('id', 'slug')},
        ),
    ]
