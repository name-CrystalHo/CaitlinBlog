# Generated by Django 3.1.4 on 2021-01-24 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0008_aboutme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='description',
            field=models.TextField(),
        ),
    ]
