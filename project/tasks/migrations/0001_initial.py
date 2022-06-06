# Generated by Django 4.0.4 on 2022-06-01 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('continent', models.IntegerField(max_length=200)),
                ('area', models.IntegerField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('popuplation', models.IntegerField(max_length=200)),
                ('countryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.country')),
            ],
        ),
    ]
