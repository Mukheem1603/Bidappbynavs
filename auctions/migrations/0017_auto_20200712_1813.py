# Generated by Django 3.0.8 on 2020-07-12 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_auto_20200712_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='lnk',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
