# Generated by Django 3.2.4 on 2021-07-03 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=18)),
                ('dob', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('desc', models.TextField()),
                ('salary', models.FloatField()),
                ('is_verify', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=18)),
                ('dob', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('desc', models.TextField()),
                ('salary', models.FloatField()),
                ('is_verify', models.BooleanField(default=False)),
            ],
        ),
    ]
