# Generated by Django 4.0.6 on 2022-07-26 14:45

import diabetics_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('left_eye', models.ImageField(blank=True, null=True, upload_to=diabetics_app.models.TEST_IMAGE_LOCATION)),
                ('right_eye', models.ImageField(blank=True, null=True, upload_to=diabetics_app.models.TEST_IMAGE_LOCATION)),
                ('result', models.CharField(max_length=500)),
                ('slug', models.SlugField(blank=True, editable=False, null=True)),
                ('tested_on', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
