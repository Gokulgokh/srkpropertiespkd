# Generated by Django 5.0 on 2024-05-03 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srkapp', '0003_product_tbl_property_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('password', models.TextField(max_length=100)),
            ],
        ),
    ]
