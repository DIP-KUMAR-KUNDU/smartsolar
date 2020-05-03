# Generated by Django 3.0.5 on 2020-05-01 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_assignuser_assign_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dcsupplyparameter',
            name='load_current_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dcsupplyparameter',
            name='load_current_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dcsupplyparameter',
            name='load_current_3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dcsupplyparameter',
            name='load_current_4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dcsupplyparameter',
            name='system_voltage',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sitedetails',
            name='distance_shed_dc_cabinate',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Record DISTANCE (Meter) from Shed leg on which DB will be fix to the DC Cabinet '),
        ),
        migrations.AlterField(
            model_name='sitedetails',
            name='height_dc_cabinet',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Measure and record the available space(HEIGHT (Meter)) for the MPPT controller in the DC cabinet'),
        ),
        migrations.AlterField(
            model_name='sitedetails',
            name='length_dc_cabinet',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Measure and record the available space(LENGTH (Meter)) for the MPPT controller in the DC cabinet'),
        ),
        migrations.AlterField(
            model_name='sitedetails',
            name='tall_structure_distance_fence',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='If there any tall structure, specify the DISTANCE (Meter) of the structure from the site fence'),
        ),
        migrations.AlterField(
            model_name='sitedetails',
            name='tall_structure_height',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='If there any tall structure, specify the HEIGHT (Meter)'),
        ),
        migrations.AlterField(
            model_name='sitedimensiondetails',
            name='back_side',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sitedimensiondetails',
            name='distance_tower_back',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sitedimensiondetails',
            name='distance_tower_front',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sitedimensiondetails',
            name='distance_tower_left',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sitedimensiondetails',
            name='distance_tower_right',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sitedimensiondetails',
            name='front_side',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sitedimensiondetails',
            name='left_side',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sitedimensiondetails',
            name='length_side_A_option_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sitedimensiondetails',
            name='length_side_A_option_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sitedimensiondetails',
            name='length_side_B_option_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sitedimensiondetails',
            name='length_side_B_option_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sitedimensiondetails',
            name='length_side_C_option_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sitedimensiondetails',
            name='length_side_C_option_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sitedimensiondetails',
            name='length_side_D_option_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sitedimensiondetails',
            name='length_side_D_option_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sitedimensiondetails',
            name='right_side',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
