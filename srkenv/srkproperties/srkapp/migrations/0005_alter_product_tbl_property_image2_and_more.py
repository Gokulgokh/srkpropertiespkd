# Generated by Django 5.0 on 2024-05-04 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srkapp', '0004_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_tbl',
            name='property_image2',
            field=models.FileField(blank=True, null=True, upload_to='pictures'),
        ),
        migrations.AlterField(
            model_name='product_tbl',
            name='property_image3',
            field=models.FileField(blank=True, null=True, upload_to='pictures'),
        ),
        migrations.AlterField(
            model_name='product_tbl',
            name='property_image4',
            field=models.FileField(blank=True, null=True, upload_to='pictures'),
        ),
        migrations.AlterField(
            model_name='product_tbl',
            name='property_image5',
            field=models.FileField(blank=True, null=True, upload_to='pictures'),
        ),
        migrations.AlterField(
            model_name='product_tbl',
            name='property_image6',
            field=models.FileField(blank=True, null=True, upload_to='pictures'),
        ),
        migrations.AlterField(
            model_name='product_tbl',
            name='property_image7',
            field=models.FileField(blank=True, null=True, upload_to='pictures'),
        ),
        migrations.AlterField(
            model_name='product_tbl',
            name='property_image8',
            field=models.FileField(blank=True, null=True, upload_to='pictures'),
        ),
    ]
