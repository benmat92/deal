# Generated by Django 3.2.4 on 2021-07-15 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_deal_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deal',
            name='author',
        ),
    ]
