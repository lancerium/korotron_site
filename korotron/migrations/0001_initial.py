# Generated by Django 3.0.7 on 2020-06-26 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('content', models.TextField(blank=True, verbose_name='Котнент')),
                ('photo', models.ImageField(blank=True, upload_to='', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Информация о нас',
            },
        ),
    ]
