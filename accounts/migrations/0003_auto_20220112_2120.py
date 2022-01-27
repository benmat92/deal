# Generated by Django 3.2.4 on 2022-01-13 03:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='about',
            field=models.TextField(blank=True, max_length=500, verbose_name='about'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=150, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
