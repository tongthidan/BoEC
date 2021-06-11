# Generated by Django 3.2.4 on 2021-06-11 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shippment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateShip', models.DateTimeField(max_length=100)),
                ('dateReceive', models.DateTimeField(max_length=100)),
                ('costShippment', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='GlobalShippment',
            fields=[
                ('shippment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Shippment.shippment')),
                ('countryReceive', models.CharField(max_length=255)),
            ],
            bases=('Shippment.shippment',),
        ),
        migrations.CreateModel(
            name='InternalShippment',
            fields=[
                ('shippment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Shippment.shippment')),
                ('distance', models.BigIntegerField()),
                ('cityReceive', models.CharField(max_length=255)),
            ],
            bases=('Shippment.shippment',),
        ),
    ]