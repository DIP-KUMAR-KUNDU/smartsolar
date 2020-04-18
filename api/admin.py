from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(SiteMaster)
admin.site.register(ContractMaster)
admin.site.register(SiteDetails)
admin.site.register(DCSupplyParameter)
admin.site.register(SiteDimensionDetails)
admin.site.register(GeographicalDetails)
admin.site.register(SupportingImagesGeographical)
admin.site.register(SiteVisit)