# Generated by Django 2.0.1 on 2018-01-20 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0003_auto_20180117_0429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_us',
            name='cust_contact_number',
            field=models.IntegerField(blank=True, max_length=12),
        ),
    ]
