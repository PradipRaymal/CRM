# Generated by Django 3.1.2 on 2020-12-08 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('barcode', models.ImageField(blank=True, upload_to='image/')),
                ('country_id', models.CharField(max_length=1, null=True)),
                ('manufacturer_id', models.CharField(max_length=6, null=True)),
                ('number_id', models.CharField(max_length=5, null=True)),
            ],
        ),
    ]