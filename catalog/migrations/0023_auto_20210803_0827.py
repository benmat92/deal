# Generated by Django 3.2.4 on 2021-08-03 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0022_deal_snippet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deal',
            name='snippet',
        ),
        migrations.AlterField(
            model_name='deal',
            name='title',
            field=models.CharField(max_length=25),
        ),
    ]