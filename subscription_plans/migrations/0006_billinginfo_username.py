# Generated by Django 4.2.5 on 2023-10-16 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription_plans', '0005_remove_billinginfo_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='billinginfo',
            name='username',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
