# Generated by Django 3.0.4 on 2020-03-24 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otherusers',
            name='last_name',
        ),
    ]
