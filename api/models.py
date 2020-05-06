from django.db import models
from django.contrib.auth.models import User
import uuid 

from django.utils import timezone

# Create your models here.
class CompanyUser(models.Model):
    user = models.OneToOneField(User, models.SET_NULL, blank=True, null=True)
    comp = models.CharField(verbose_name="Company Name", max_length=30, choices=(
    ("VYOMA", "VYOMA"),
    ("PARK", "PARK"),
    ("ATC", "ATC")
    ))
    role = models.CharField(verbose_name="User role in application", max_length=30, choices=(
    ("VIEW", "VIEW"),
    ("ASSIGN", "ASSIGN"),
    ), null=True)

    def __str__(self):
        return self.user.username



class SiteMaster(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    site_id = models.CharField(max_length=50, unique=True)
    site_name = models.CharField(max_length=50, blank=True, null=True)
    site_region = models.CharField(max_length=50, blank=True, null=True)
    site_latitude = models.CharField(
        max_length=30, blank=True, null=True)
    site_longitude = models.CharField(
        max_length=30, blank=True, null=True)

    def __str__(self):
        return self.site_id

    def natural_key(self):
        return ({"site_id": self.site_id, "site_name": self.site_name, "site_region": self.site_region, "site_latitude": self.site_latitude, "site_longitude": self.site_longitude})


class ContractMaster(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    contractor = models.CharField(max_length=100, blank=True, null=True)
    contractor_rep = models.CharField(
        verbose_name="Names of Contractor Rep",
        max_length=100, blank=True, null=True)
    contact_contractor_rep = models.CharField(
        verbose_name="Contact of Contractor Rep",
        max_length=13, blank=True, null=True)
    
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
    length_dc_cabinet = models.CharField(max_length=100,
        verbose_name="Measure and record the available space(LENGTH (Meter)) for the MPPT controller in the DC cabinet",
        blank=True, null=True)
    height_dc_cabinet = models.CharField(max_length=100,
        verbose_name="Measure and record the available space(HEIGHT (Meter)) for the MPPT controller in the DC cabinet",
        blank=True, null=True)
    tall_structure = models.BooleanField(
        verbose_name="Is there any tall structure, tree or building higher than the site fence that can cause possible shading?",
        blank=True, null=True)
    tall_structure_name = models.CharField(
        verbose_name="If there any tall structure, indicate or name the structure type(s)",
        max_length=100, blank=True, null=True)
    tall_structure_height = models.CharField(max_length=100,
        verbose_name="If there any tall structure, specify the HEIGHT (Meter)",
        blank=True, null=True)
    tall_structure_distance_fence = models.CharField(max_length=100,
        verbose_name="If there any tall structure, specify the DISTANCE (Meter) of the structure from the site fence",
        blank=True, null=True)
    distance_shed_dc_cabinate = models.CharField(max_length=100,
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
    system_voltage_comment = models.CharField(max_length=100, blank=True, null=True)
    load_current_1 = models.FloatField(blank=True, null=True)
    load_current_1_comment = models.CharField(max_length=100, blank=True, null=True)
    load_current_2 = models.FloatField(blank=True, null=True)
    load_current_2_comment = models.CharField(max_length=100, blank=True, null=True)
    load_current_3 = models.FloatField(blank=True, null=True)
    load_current_3_comment = models.CharField(max_length=100, blank=True, null=True)
    load_current_4 = models.FloatField(blank=True, null=True)
    load_current_4_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "DCSupplyParameter object " + str(self.id)


class SiteDimensionDetails(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    front_side = models.CharField(max_length=100, blank=True, null=True)
    right_side = models.CharField(max_length=100, blank=True, null=True)
    back_side = models.CharField(max_length=100, blank=True, null=True)
    left_side = models.CharField(max_length=100, blank=True, null=True)
    distance_tower_front = models.CharField(max_length=100, blank=True, null=True)
    distance_tower_right = models.CharField(max_length=100, blank=True, null=True)
    distance_tower_back = models.CharField(max_length=100, blank=True, null=True)
    distance_tower_left = models.CharField(max_length=100, blank=True, null=True)
    length_side_A_option_1 = models.CharField(max_length=100, blank=True, null=True)
    length_side_B_option_1 = models.CharField(max_length=100, blank=True, null=True)
    length_side_C_option_1 = models.CharField(max_length=100, blank=True, null=True)
    length_side_D_option_1 = models.CharField(max_length=100, blank=True, null=True)
    length_side_A_option_2 = models.CharField(max_length=100, blank=True, null=True)
    length_side_B_option_2 = models.CharField(max_length=100, blank=True, null=True)
    length_side_C_option_2 = models.CharField(max_length=100, blank=True, null=True)
    length_side_D_option_2 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "SiteDimensionDetails object " + str(self.id)



def site_id_directory_path_for_geographical_details(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/geographical_image/{1}'.format(instance.site.site_id, filename)



class GeographicalDetails(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    site = models.ForeignKey(SiteMaster, on_delete=models.CASCADE, null=True, blank=True)
    sketch_1 = models.ImageField(upload_to=site_id_directory_path_for_geographical_details, blank=True, null=True)
    sketch_2 = models.ImageField(upload_to=site_id_directory_path_for_geographical_details, blank=True, null=True)
    sketch_3 = models.ImageField(upload_to=site_id_directory_path_for_geographical_details, blank=True, null=True)
    sketch_4 = models.ImageField(upload_to=site_id_directory_path_for_geographical_details, blank=True, null=True)

    def __str__(self):
        return "GeographicalDetails object " + str(self.id)



def site_id_directory_path_for_form_details(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/form_image/{1}'.format(instance.site.site_id, filename)


class FormPhotos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    site = models.ForeignKey(SiteMaster, on_delete=models.CASCADE, null=True, blank=True)
    form_1 = models.ImageField(upload_to=site_id_directory_path_for_form_details, blank=True, null=True)
    form_2 = models.ImageField(upload_to=site_id_directory_path_for_form_details, blank=True, null=True)
    form_3 = models.ImageField(upload_to=site_id_directory_path_for_form_details, blank=True, null=True)
    form_4 = models.ImageField(upload_to=site_id_directory_path_for_form_details, blank=True, null=True)
    form_5 = models.ImageField(upload_to=site_id_directory_path_for_form_details, blank=True, null=True)

    def __str__(self):
        return "FormPhotos object " + str(self.id)




class SiteVisit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    site = models.ForeignKey(SiteMaster, on_delete=models.CASCADE, blank=True, null=True)
    contract = models.ForeignKey(ContractMaster, on_delete=models.CASCADE, blank=True, null=True)
    details = models.ForeignKey(SiteDetails, on_delete=models.CASCADE, blank=True, null=True)
    dcsupply = models.ForeignKey(DCSupplyParameter, on_delete=models.CASCADE, blank=True, null=True)
    dimension = models.ForeignKey(SiteDimensionDetails, on_delete=models.CASCADE, blank=True, null=True)
    geography = models.ForeignKey(GeographicalDetails, on_delete=models.CASCADE, blank=True, null=True)
    form = models.ForeignKey(FormPhotos, on_delete=models.CASCADE, blank=True, null=True)
    visited = models.DateTimeField(default=timezone.now, unique=True)
    status_stage = models.SmallIntegerField(default=4)
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)



def site_id_directory_path_for_image_pool(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/image_pool/{1}'.format(instance.sitevisit.site.site_id, filename)



class SiteVisitImagePool(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sitevisit = models.ForeignKey(SiteVisit, on_delete=models.CASCADE, blank=True, null=True)
    supporting_images = models.ImageField(upload_to=site_id_directory_path_for_image_pool)





class AssignUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    site_visit = models.ForeignKey(SiteVisit, on_delete=models.CASCADE, blank=True, null=True)
    assigned = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    task = models.CharField(max_length=100)
    comment = models.TextField(blank=True, null=True)
    assign_at = models.DateTimeField(auto_now_add=True, null=True)