from django.db import models
from django.contrib.auth.models import User
import uuid 

from django.utils import timezone

# Create your models here.


class SiteMaster(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    site_id = models.CharField(max_length=50, unique=True)
    site_name = models.CharField(max_length=50, blank=True, null=True)
    site_region = models.CharField(max_length=50, blank=True, null=True)
    site_latitude = models.DecimalField(
        max_digits=22, decimal_places=16, blank=True, null=True)
    site_longitude = models.DecimalField(
        max_digits=22, decimal_places=16, blank=True, null=True)

    def __str__(self):
        return self.site_id

    def natural_key(self):
        return ({"site_id": self.site_id, "site_name": self.site_name, "site_region": self.site_region, "site_latitude": self.site_latitude, "site_longitude": self.site_longitude})


class ContractMaster(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    contractor = models.CharField(max_length=100)
    contractor_rep = models.CharField(
        verbose_name="Names of Contractor Rep",
        max_length=100)
    contact_contractor_rep = models.CharField(
        verbose_name="Contact of Contractor Rep",
        max_length=13)
    
    class Meta:
        unique_together = ('contractor', 'contractor_rep', 'contact_contractor_rep')

    def __str__(self):
        return self.contractor

    def natural_key(self):
        return ({"contractor": self.contractor, "contractor_rep": self.contractor_rep, "contact_contractor_rep": self.contact_contractor_rep})


class SiteDetails(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dc_system_on_site = models.BooleanField(blank=True, null=True)
    dc_system_brand = models.CharField(max_length=50, blank=True, null=True)
    dc_system_size = models.CharField(max_length=50, blank=True, null=True)
    space_avail_in_dc_cabinet = models.BooleanField(
        verbose_name="Is space available inside the DC Cabinet for Solar MPPT Controller to be installed at the power compartment section",
        blank=True, null=True)
    length_dc_cabinet = models.FloatField(
        verbose_name="Measure and record the available space(LENGTH (Meter)) for the MPPT controller in the DC cabinet",
        blank=True, null=True)
    height_dc_cabinet = models.FloatField(
        verbose_name="Measure and record the available space(HEIGHT (Meter)) for the MPPT controller in the DC cabinet",
        blank=True, null=True)
    tall_structure = models.BooleanField(
        verbose_name="Is there any tall structure, tree or building higher than the site fence that can cause possible shading?",
        blank=True, null=True)
    tall_structure_name = models.CharField(
        verbose_name="If there any tall structure, indicate or name the structure type(s)",
        max_length=100, blank=True, null=True)
    tall_structure_height = models.FloatField(
        verbose_name="If there any tall structure, specify the HEIGHT (Meter)",
        blank=True, null=True)
    tall_structure_distance_fence = models.FloatField(
        verbose_name="If there any tall structure, specify the DISTANCE (Meter) of the structure from the site fence",
        blank=True, null=True)
    distance_shed_dc_cabinate = models.FloatField(
        verbose_name="Record DISTANCE (Meter) from Shed leg on which DB will be fix to the DC Cabinet ",
        blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return "SiteDetails object " + str(self.id)

    # def natural_key(self):
    #     return ({})


class DCSupplyParameter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    system_voltage = models.FloatField(blank=True, null=True)
    load_current_1 = models.FloatField(blank=True, null=True)
    load_current_2 = models.FloatField(blank=True, null=True)
    load_current_3 = models.FloatField(blank=True, null=True)
    load_current_4 = models.FloatField(blank=True, null=True)

    def __str__(self):
        return "DCSupplyParameter object " + str(self.id)


class SiteDimensionDetails(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    front_side = models.FloatField(blank=True, null=True)
    right_side = models.FloatField(blank=True, null=True)
    back_side = models.FloatField(blank=True, null=True)
    left_side = models.FloatField(blank=True, null=True)
    distance_tower_front = models.FloatField(blank=True, null=True)
    distance_tower_right = models.FloatField(blank=True, null=True)
    distance_tower_back = models.FloatField(blank=True, null=True)
    distance_tower_left = models.FloatField(blank=True, null=True)
    length_side_A_option_1 = models.FloatField(blank=True, null=True)
    length_side_B_option_1 = models.FloatField(blank=True, null=True)
    length_side_C_option_1 = models.FloatField(blank=True, null=True)
    length_side_D_option_1 = models.FloatField(blank=True, null=True)
    length_side_A_option_2 = models.FloatField(blank=True, null=True)
    length_side_B_option_2 = models.FloatField(blank=True, null=True)
    length_side_C_option_2 = models.FloatField(blank=True, null=True)
    length_side_D_option_2 = models.FloatField(blank=True, null=True)

    def __str__(self):
        return "SiteDimensionDetails object " + str(self.id)


class GeographicalDetails(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sketch_1 = models.ImageField(blank=True, null=True)
    sketch_2 = models.ImageField(blank=True, null=True)
    sketch_3 = models.ImageField(blank=True, null=True)
    sketch_4 = models.ImageField(blank=True, null=True)

    def __str__(self):
        return "GeographicalDetails object " + str(self.id)


class SupportingImagesGeographical(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    geographicaldetails = models.ForeignKey(GeographicalDetails, on_delete=models.CASCADE)
    supporting_images = models.ImageField()
    supporting_images_caption = models.CharField(max_length=300)



class SiteVisit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    site = models.ForeignKey(SiteMaster, on_delete=models.CASCADE)
    contract = models.ForeignKey(ContractMaster, on_delete=models.CASCADE)
    details = models.ForeignKey(SiteDetails, on_delete=models.CASCADE)
    dcsupply = models.ForeignKey(DCSupplyParameter, on_delete=models.CASCADE)
    dimension = models.ForeignKey(SiteDimensionDetails, on_delete=models.CASCADE)
    geography = models.ForeignKey(GeographicalDetails, on_delete=models.CASCADE)
    visited = models.DateTimeField(default=timezone.now, unique=True)

    class Meta:
        unique_together = ('site', 'contract', 'details', 'dcsupply', 'dimension', 'geography')