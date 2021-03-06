# Generated by Django 3.0.5 on 2020-05-06 18:48

import api.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_geographicaldetails_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractmaster',
            name='contact_contractor_rep',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='Contact of Contractor Rep'),
        ),
        migrations.AlterField(
            model_name='contractmaster',
            name='contractor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contractmaster',
            name='contractor_rep',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Names of Contractor Rep'),
        ),
        migrations.AlterField(
            model_name='sitevisit',
            name='contract',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.ContractMaster'),
        ),
        migrations.AlterField(
            model_name='sitevisit',
            name='dcsupply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.DCSupplyParameter'),
        ),
        migrations.AlterField(
            model_name='sitevisit',
            name='details',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.SiteDetails'),
        ),
        migrations.AlterField(
            model_name='sitevisit',
            name='dimension',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.SiteDimensionDetails'),
        ),
        migrations.AlterField(
            model_name='sitevisit',
            name='geography',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.GeographicalDetails'),
        ),
        migrations.AlterField(
            model_name='sitevisit',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.SiteMaster'),
        ),
        migrations.AlterUniqueTogether(
            name='sitevisit',
            unique_together=set(),
        ),
        migrations.CreateModel(
            name='FormPhotos',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('form_1', models.ImageField(blank=True, null=True, upload_to=api.models.site_id_directory_path_for_form_details)),
                ('form_2', models.ImageField(blank=True, null=True, upload_to=api.models.site_id_directory_path_for_form_details)),
                ('form_3', models.ImageField(blank=True, null=True, upload_to=api.models.site_id_directory_path_for_form_details)),
                ('form_4', models.ImageField(blank=True, null=True, upload_to=api.models.site_id_directory_path_for_form_details)),
                ('form_5', models.ImageField(blank=True, null=True, upload_to=api.models.site_id_directory_path_for_form_details)),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.SiteMaster')),
            ],
        ),
        migrations.AddField(
            model_name='sitevisit',
            name='form',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.FormPhotos'),
        ),
    ]
