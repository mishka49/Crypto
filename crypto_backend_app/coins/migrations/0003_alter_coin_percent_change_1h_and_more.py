# Generated by Django 4.2.10 on 2024-03-05 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0002_alter_coin_percent_change_1h_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='percent_change_1h',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='coin',
            name='percent_change_24h',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='coin',
            name='percent_change_7d',
            field=models.CharField(max_length=20),
        ),
    ]
