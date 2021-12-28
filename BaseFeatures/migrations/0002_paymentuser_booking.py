# Generated by Django 4.0 on 2021-12-28 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
        ('BaseFeatures', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardName', models.CharField(max_length=100)),
                ('cardNumber', models.CharField(max_length=100)),
                ('expirationDate', models.CharField(max_length=100)),
                ('cvv', models.CharField(max_length=3)),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.person')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BaseFeatures.paymentuser')),
                ('routeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BaseFeatures.planroute')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.person')),
            ],
        ),
    ]