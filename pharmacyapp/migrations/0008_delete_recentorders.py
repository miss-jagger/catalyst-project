# Generated by Django 4.2 on 2023-04-26 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacyapp', '0007_alter_recentorders_quantitybought'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RecentOrders',
        ),
    ]