# Generated by Django 5.0.3 on 2024-08-08 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='media')),
                ('size', models.CharField(max_length=10)),
                ('category', models.CharField(choices=[('mens', 'mens'), ('womens', 'womens'), ('kids', 'kids'), ('electronic', 'electronic'), ('special_product', 'special_product')], max_length=50)),
                ('is_avaliable', models.BooleanField()),
            ],
        ),
    ]
