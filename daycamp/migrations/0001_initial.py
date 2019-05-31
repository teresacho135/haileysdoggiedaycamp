# Generated by Django 2.2.1 on 2019-05-30 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('isActive', models.BooleanField(default=False)),
                ('food_amount', models.CharField(max_length=100)),
                ('medicine', models.TextField()),
                ('owner', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_total', models.IntegerField()),
                ('hours_total', models.IntegerField()),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.IntegerField()),
                ('days', models.IntegerField()),
            ],
        ),
    ]
