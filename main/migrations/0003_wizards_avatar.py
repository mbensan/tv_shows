# Generated by Django 3.2.5 on 2021-08-19 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210817_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='wizards',
            name='avatar',
            field=models.URLField(default='https://partfy.com/blog/wp-content/uploads/2020/05/mejoresmagosespa%C3%B1oles-1000x550.jpg'),
        ),
    ]
