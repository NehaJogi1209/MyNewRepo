# Generated by Django 2.2.7 on 2021-03-15 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CountryModel',
            fields=[
                ('cid', models.IntegerField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'COUNTRY',
            },
        ),
        migrations.CreateModel(
            name='StateModel',
            fields=[
                ('sid', models.IntegerField(primary_key=True, serialize=False)),
                ('state', models.CharField(max_length=50)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='states', to='producer.CountryModel')),
            ],
            options={
                'db_table': 'STATE',
            },
        ),
        migrations.CreateModel(
            name='CityModel',
            fields=[
                ('ctid', models.IntegerField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=50)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='producer.StateModel')),
            ],
            options={
                'db_table': 'CITY',
            },
        ),
    ]
