# Generated by Django 4.0 on 2021-12-28 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
        ('BaseFeatures', '0002_paymentuser_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationsUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1000)),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.person')),
            ],
        ),
    ]
