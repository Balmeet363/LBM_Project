# Generated by Django 3.0.6 on 2020-06-25 18:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0007_auto_20200625_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issuebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issuedate', models.DateField(blank=True, default=datetime.datetime(2020, 6, 25, 14, 37, 15, 667975))),
                ('expirydate', models.DateField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Library.Book')),
                ('patron', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Library.Patron')),
            ],
            options={
                'db_table': 'issuedbooks',
            },
        ),
    ]
