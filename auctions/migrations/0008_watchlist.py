# Generated by Django 3.0.8 on 2020-07-11 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usrs1', models.CharField(max_length=64)),
                ('titlee', models.CharField(max_length=64)),
            ],
        ),
    ]