# Generated by Django 4.2.1 on 2023-05-13 08:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeuser',
            name='follows',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='suivi'),
        ),
        migrations.AlterField(
            model_name='customeuser',
            name='username',
            field=models.CharField(max_length=128, unique=True, verbose_name="Nom d'utilisateur"),
        ),
    ]
