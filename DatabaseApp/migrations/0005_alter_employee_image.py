# Generated by Django 4.0.1 on 2022-04-14 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DatabaseApp', '0004_remove_employee_field_employee_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]