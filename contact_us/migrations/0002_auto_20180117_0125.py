# Generated by Django 2.0.1 on 2018-01-17 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_us',
            name='cust_contact_number',
            field=models.IntegerField(),
        ),
    ]
