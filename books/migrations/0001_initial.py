# Generated by Django 4.0.1 on 2022-01-25 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=100)),
                ('pages', models.IntegerField(max_length=50)),
                ('book_cover', models.ImageField(upload_to='images/')),
                ('storyline', models.TextField()),
            ],
        ),
    ]
