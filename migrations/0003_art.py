# Generated by Django 3.0.8 on 2021-03-29 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0002_auto_20210328_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('a_id', models.AutoField(primary_key=True, serialize=False)),
                ('a_name', models.CharField(max_length=30)),
                ('a_price', models.IntegerField(max_length=10)),
                ('a_phone', models.IntegerField(max_length=20)),
                ('a_address', models.CharField(max_length=120)),
                ('a_condition', models.CharField(max_length=255)),
                ('a_description', models.CharField(max_length=255)),
                ('a_recentwork', models.ImageField(upload_to='artist/images')),
                ('a_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.Services')),
            ],
        ),
    ]
