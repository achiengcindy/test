# Generated by Django 2.1.7 on 2019-05-06 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_meta_keywords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='credit',
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
    ]
