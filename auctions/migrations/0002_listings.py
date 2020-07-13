# Generated by Django 3.0.8 on 2020-07-10 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('desc', models.CharField(max_length=64)),
                ('bid', models.IntegerField()),
                ('cat', models.CharField(max_length=64)),
                ('ur', models.CharField(max_length=64)),
            ],
        ),
    ]