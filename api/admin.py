from django.contrib import admin

from .models import *


admin.site.site_header = "iSmart Site Administration"

# Register your models here.


class SiteMasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_id', 'site_name', 'site_region', 'site_latitude' ,'site_longitude')
admin.site.register(SiteMaster, SiteMasterAdmin)



class ContractMasterAdmin(admin.ModelAdmin):
    list_display = ('id'
,'contractor'
,'contractor_rep'
,'contact_contractor_rep')
admin.site.register(ContractMaster, ContractMasterAdmin)



class SiteDetailsAdmin(admin.ModelAdmin):
    list_display = ('id'
,'dc_system_on_site'
,'dc_system_brand'
,'dc_system_size'
,'space_avail_in_dc_cabinet'
,'length_dc_cabinet'
,'height_dc_cabinet'
,'tall_structure'
,'tall_structure_name'
,'tall_structure_height'
,'tall_structure_distance_fence'
,'distance_shed_dc_cabinate'
,'comment')
admin.site.register(SiteDetails, SiteDetailsAdmin)



class DCSupplyParameterAdmin(admin.ModelAdmin):
    list_display = ('id'
,'system_voltage', 'system_voltage_comment',
'load_current_1', 'load_current_1_comment',
'load_current_2', 'load_current_2_comment',
'load_current_3', 'load_current_3_comment',
'load_current_4', 'load_current_4_comment')
admin.site.register(DCSupplyParameter, DCSupplyParameterAdmin)



class SiteDimensionDetailsAdmin(admin.ModelAdmin):
    list_display = ('id'
,'front_side'
,'right_side'
,'back_side'
,'left_side'
,'distance_tower_front'
,'distance_tower_right'
,'distance_tower_back'
,'distance_tower_left'
,'length_side_A_option_1'
,'length_side_B_option_1'
,'length_side_C_option_1'
,'length_side_D_option_1'
,'length_side_A_option_2'
,'length_side_B_option_2'
,'length_side_C_option_2'
,'length_side_D_option_2')
admin.site.register(SiteDimensionDetails, SiteDimensionDetailsAdmin)



class GeographicalDetailsAdmin(admin.ModelAdmin):
    list_display = ("id"
,"sketch_1"
,"sketch_2"
,"sketch_3"
,"sketch_4")
admin.site.register(GeographicalDetails, GeographicalDetailsAdmin)



class SupportingImagesGeographicalAdmin(admin.ModelAdmin):
    list_display = ('id', 'geographicaldetails', 'supporting_images', 'supporting_images_caption')
    list_display_links = ('id', 'geographicaldetails', 'supporting_images', 'supporting_images_caption')
admin.site.register(SupportingImagesGeographical, SupportingImagesGeographicalAdmin)



class SiteVisitAdmin(admin.ModelAdmin):
    list_display = ('id','site'
,'contract'
,'details'
,'dcsupply'
,'dimension'
,'geography','visited'
,'status_stage')
    list_display_links = ('id','site'
,'contract'
,'details'
,'dcsupply'
,'dimension'
,'geography','visited'
,'status_stage')
admin.site.register(SiteVisit, SiteVisitAdmin)



class CompanyUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'comp', 'role')
    list_display_links = ('id', 'user', 'comp', 'role')
admin.site.register(CompanyUser, CompanyUserAdmin)



class AssignUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_visit', 'assigned', 'task', 'comment', 'assign_at')
    list_display_links = ('id', 'site_visit', 'assigned', 'task', 'comment', 'assign_at')
admin.site.register(AssignUser, AssignUserAdmin)


