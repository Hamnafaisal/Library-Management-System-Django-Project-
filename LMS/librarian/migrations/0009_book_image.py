# Generated by Django 3.1 on 2020-08-28 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0008_book_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
