# Generated by Django 2.1.7 on 2019-05-07 12:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.AddField(
            model_name='comment',
            name='commenter',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
