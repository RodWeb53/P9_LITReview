# Generated by Django 4.2.1 on 2023-05-17 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_alter_ticket_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='body',
            field=models.TextField(blank=True, max_length=8192),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Titre'),
        ),
    ]
