# Generated by Django 4.0.4 on 2022-05-20 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='brand',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='store.brand'),
            preserve_default=False,
        ),
    ]
