# Generated by Django 3.0.5 on 2020-04-27 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_assignuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignuser',
            name='compuser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.CompanyUser'),
        ),
    ]
