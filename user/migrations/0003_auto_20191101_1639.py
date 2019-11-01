# Generated by Django 2.2.6 on 2019-11-01 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20191101_1506'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.SlugField(blank=True, default=None, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[(None, '-'), ('M', 'Male'), ('F', 'Female')], default=None, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='hobbie',
            field=models.CharField(blank=True, choices=[('sport', 'Sport'), ('games', 'Computer Games')], default='Sport', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('username', 'email')},
        ),
    ]
