# Generated by Django 4.0.1 on 2022-04-14 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DatabaseApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='field',
            field=models.ImageField(default='max', upload_to=''),
        ),
    ]
