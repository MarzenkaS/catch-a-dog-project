# Generated by Django 4.2.10 on 2024-07-26 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0010_alter_reviews_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='image',
        ),
    ]
