# Generated by Django 2.2 on 2021-03-26 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('category', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'dph_products',
            },
        ),
    ]
