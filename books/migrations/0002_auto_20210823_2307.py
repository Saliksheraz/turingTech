# Generated by Django 3.1.7 on 2021-08-23 18:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='val',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='volume',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.volume'),
        ),
    ]