# Generated by Django 3.0.7 on 2020-06-29 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('korotron', '0008_action_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AddField(
            model_name='action',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AddField(
            model_name='services',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
    ]
