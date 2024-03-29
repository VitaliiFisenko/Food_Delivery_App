# Generated by Django 2.2.6 on 2019-11-11 22:14

import django.core.validators
from django.db import migrations, models
import django_extensions.db.fields.json
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('comment', models.TextField(blank=True)),
                ('name', models.CharField(max_length=20)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('status', models.CharField(choices=[('done', 'Done'), ('in_process', 'In process')], default='in_process', max_length=20)),
                ('products', django_extensions.db.fields.json.JSONField(default={'name': 5}, null=True)),
                ('payment', models.CharField(choices=[('card', 'By card'), ('cash', 'By cash'), ('bonuses', 'By bonuses')], default='cash', max_length=10)),
                ('card_number', models.BigIntegerField(blank=True, default=0, help_text='Such as 1234567812345678', validators=[django.core.validators.RegexValidator('^\\d{16}$', 'Wrong card number')])),
                ('card_date', models.CharField(blank=True, help_text='Such as 11/11', max_length=5, validators=[django.core.validators.RegexValidator('^\\d{2}/\\d{2}$', 'Wrong date')])),
                ('card_cvs', models.IntegerField(blank=True, default=0, help_text='Such as 913', validators=[django.core.validators.RegexValidator('^\\d{3}$')])),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
            ],
        ),
    ]
