# Generated by Django 2.2.6 on 2020-05-02 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0002_auto_20200501_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_image',
            field=models.ImageField(default='DEFAULT VALUE', upload_to='book_images'),
        ),
    ]
