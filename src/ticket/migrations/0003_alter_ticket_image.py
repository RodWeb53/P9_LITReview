# Generated by Django 4.2.1 on 2023-05-13 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_alter_ticket_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]