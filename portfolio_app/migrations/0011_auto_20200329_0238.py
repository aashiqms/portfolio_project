# Generated by Django 3.0.4 on 2020-03-29 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0010_remove_feedback_happy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='email',
        ),
        migrations.AddField(
            model_name='feedback',
            name='customer_name_optional',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='email_optional',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
