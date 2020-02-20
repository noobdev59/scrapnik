# Generated by Django 3.0.3 on 2020-02-20 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0005_auto_20200220_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='table',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.TableBrand'),
        ),
    ]
