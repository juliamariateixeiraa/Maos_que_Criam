# Generated by Django 5.1 on 2024-10-15 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app15', '0004_doador_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='doador',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='doador',
            name='endereco',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
