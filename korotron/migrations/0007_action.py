# Generated by Django 3.0.7 on 2020-06-29 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('korotron', '0006_services_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='', verbose_name='Картинка акции')),
            ],
            options={
                'verbose_name': 'Акция',
                'verbose_name_plural': 'Акции',
            },
        ),
    ]
