# Generated by Django 3.2 on 2022-07-07 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sokoapp', '0014_auto_20220707_0900'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartproduct',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
