# Generated by Django 3.2.4 on 2021-07-23 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0019_alter_comment_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='deal',
        ),
    ]
