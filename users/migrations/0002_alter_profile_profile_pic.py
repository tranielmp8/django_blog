# Generated by Django 4.0.3 on 2022-06-06 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='pictures/spade.png', upload_to='pictures'),
        ),
    ]
