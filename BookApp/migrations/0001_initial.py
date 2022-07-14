# Generated by Django 4.0.6 on 2022-07-11 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('BookId', models.AutoField(primary_key=True, serialize=False)),
                ('BookName', models.CharField(max_length=500)),
                ('Quantity', models.BigIntegerField()),
                ('BookGenre', models.CharField(max_length=500)),
                ('IsBestSeller', models.BooleanField(max_length=500)),
                ('CreatedAt', models.DateField()),
                ('UpdatedAt', models.DateField()),
            ],
        ),
    ]
