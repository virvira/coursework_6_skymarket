# Generated by Django 3.2.6 on 2023-03-04 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ads', '0004_alter_ad_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='ad',
            name='price',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='ad',
            name='title',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
