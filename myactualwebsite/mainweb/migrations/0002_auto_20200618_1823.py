# Generated by Django 3.0.6 on 2020-06-18 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainweb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospect',
            name='interest_area',
            field=models.TextField(max_length=200),
        ),
    ]
