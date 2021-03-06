# Generated by Django 3.1 on 2020-08-23 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=10)),
                ('branch', models.CharField(max_length=3)),
                ('contact_no', models.CharField(max_length=10)),
                ('total_books_due', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
