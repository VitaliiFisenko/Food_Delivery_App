# Generated by Django 2.2.6 on 2019-11-11 15:00

import django.core.validators
from django.db import migrations, models
import django_extensions.db.fields
import django_extensions.db.fields.json
import product.add_functions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
                ('image', models.ImageField(default='product/images/no_image.png', upload_to='')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=product.add_functions.get_additional_images_path)),
            ],
            options={
                'verbose_name_plural': 'images',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField(default='No description')),
                ('short_description', models.CharField(default='No description', max_length=200)),
                ('main_photo', models.ImageField(default='product/images/no_image.png', upload_to=product.add_functions.get_image_path)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=11, validators=[django.core.validators.MinValueValidator(0, 'Wrong price')])),
                ('composition', django_extensions.db.fields.json.JSONField(default={'calories': 0, 'carbohydrates': 0, 'fats': 0, 'proteins': 0, 'weight': 0}, null=True)),
                ('views', models.IntegerField(default=0)),
                ('to_remove', models.BooleanField(default=False, verbose_name='Marked for deleting')),
                ('categories', models.ManyToManyField(related_name='products', to='product.Category')),
            ],
            options={
                'verbose_name_plural': 'products',
            },
        ),
    ]
