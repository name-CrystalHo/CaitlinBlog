# Generated by Django 3.1.4 on 2021-04-08 19:17

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0013_auto_20210204_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='article_text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
