# Generated by Django 5.0.4 on 2024-04-26 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ferramentas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ferramenta',
            old_name='rotulo',
            new_name='codigo',
        ),
    ]
