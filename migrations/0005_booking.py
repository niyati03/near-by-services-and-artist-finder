# Generated by Django 3.0.8 on 2021-03-29 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0004_auto_20210329_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('booking_user', models.CharField(max_length=40)),
                ('booking_phone', models.IntegerField()),
                ('booking_address', models.CharField(max_length=255)),
                ('booking_date_of_service', models.DateField()),
                ('booking_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.Art')),
            ],
        ),
    ]
