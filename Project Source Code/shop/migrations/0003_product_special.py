# Generated by Django 2.2 on 2019-04-26 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='special',
            field=models.BooleanField(default=False),
        ),
    ]
