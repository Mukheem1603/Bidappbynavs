# Generated by Django 3.0.8 on 2020-07-12 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auto_20200712_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Winners1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userwin', models.CharField(max_length=64)),
                ('tll', models.CharField(max_length=64)),
                ('desc1', models.CharField(max_length=64)),
                ('bidd', models.IntegerField()),
                ('cat1', models.CharField(max_length=64)),
                ('lnk1', models.CharField(max_length=64)),
            ],
        ),
        migrations.DeleteModel(
            name='Winners',
        ),
    ]
