# Generated by Django 3.0.4 on 2020-03-29 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0011_auto_20200329_0238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='customer_name_optional',
            new_name='name_optional',
        ),
    ]
