# Generated by Django 4.2.6 on 2023-10-30 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]