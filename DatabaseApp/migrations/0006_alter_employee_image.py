# Generated by Django 4.0.1 on 2022-04-14 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DatabaseApp', '0005_alter_employee_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
