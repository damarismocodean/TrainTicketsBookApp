# Generated by Django 4.0 on 2021-12-27 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stationName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destinationStationID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinationStation', to='BaseFeatures.station')),
                ('startStationID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='startStation', to='BaseFeatures.station')),
                ('trainID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BaseFeatures.train')),
            ],
        ),
        migrations.CreateModel(
            name='PlanRoute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.CharField(max_length=100)),
                ('arrivalTime', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('routeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BaseFeatures.route')),
            ],
        ),
    ]
