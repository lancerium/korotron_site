# Generated by Django 3.0.7 on 2020-07-01 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('korotron', '0011_auto_20200630_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoryservice',
            name='link',
        ),
    ]
