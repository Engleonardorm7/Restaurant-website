# Generated by Django 5.0.2 on 2024-02-21 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0002_rename_menu_menuitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]