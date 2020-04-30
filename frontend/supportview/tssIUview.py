from django.shortcuts import render, redirect
from django.http import HttpResponse

from api.models import *
from django.conf import settings
import os

import datetime

def tssEntry(request):
    if request.method == 'POST':
        try:
            site_id = request.POST['site_id']
        except:
            site_id = ''
        try:
            site_name = request.POST['site_name']
        except:
            site_name = ''
        try:
            visited_date = request.POST['visited_date']
        except:
            visited_date = ''
        try:
            visited_time = request.POST['visited_time']
        except:
            visited_time = ''
        try:
            site_region = request.POST['site_region']
        except:
            site_region = ''
        try:
            site_latitude = request.POST['site_latitude']
        except:
            site_latitude = ''
        try:
            site_longitude = request.POST['site_longitude']
        except:
            site_longitude = ''
        try:
            contractor = request.POST['contractor']
        except:
            contractor = ''
        try:
            contractor_rep = request.POST['contractor_rep']
        except:
            contractor_rep = ''
        try:
            contact_contractor_rep = request.POST['contact_contractor_rep']
        except:
            contact_contractor_rep = ''
        try:
            dc_system_on_site = request.POST['dc_system_on_site']
        except:
            dc_system_on_site = ''
        try:
            dc_system_brand = request.POST['dc_system_brand']
        except:
            dc_system_brand = ''
        try:
            dc_system_size = request.POST['dc_system_size']
        except:
            dc_system_size = ''
        try:
            space_avail_in_dc_cabinet = request.POST['space_avail_in_dc_cabinet']
        except:
            space_avail_in_dc_cabinet = ''
        try:
            length_dc_cabinet = request.POST['length_dc_cabinet']
        except:
            length_dc_cabinet = ''
        try:
            height_dc_cabinet = request.POST['height_dc_cabinet']
        except:
            height_dc_cabinet = ''
        try:
            tall_structure = request.POST['tall_structure']
        except:
            tall_structure = ''
        try:
            tall_structure_name = request.POST['tall_structure_name']
        except:
            tall_structure_name = ''
        try:
            tall_structure_height = request.POST['tall_structure_height']
        except:
            tall_structure_height = ''
        try:
            tall_structure_distance_fence = request.POST['tall_structure_distance_fence']
        except:
            tall_structure_distance_fence = ''
        try:
            distance_shed_dc_cabinate = request.POST['distance_shed_dc_cabinate']
        except:
            distance_shed_dc_cabinate = ''
        try:
            comment = request.POST['comment']
        except:
            comment = ''
        try:
            system_voltage = request.POST['system_voltage']
        except:
            system_voltage = ''
        try:
            load_current_1 = request.POST['load_current_1']
        except:
            load_current_1 = ''
        try:
            load_current_2 = request.POST['load_current_2']
        except:
            load_current_2 = ''
        try:
            load_current_3 = request.POST['load_current_3']
        except:
            load_current_3 = ''
        try:
            load_current_4 = request.POST['load_current_4']
        except:
            load_current_4 = ''
        try:
            front_side = request.POST['front_side']
        except:
            front_side = ''
        try:
            right_side = request.POST['right_side']
        except:
            right_side = ''
        try:
            back_side = request.POST['back_side']
        except:
            back_side = ''
        try:
            left_side = request.POST['left_side']
        except:
            left_side = ''
        try:
            distance_tower_front = request.POST['distance_tower_front']
        except:
            distance_tower_front = ''
        try:
            distance_tower_right = request.POST['distance_tower_right']
        except:
            distance_tower_right = ''
        try:
            distance_tower_back = request.POST['distance_tower_back']
        except:
            distance_tower_back = ''
        try:
            distance_tower_left = request.POST['distance_tower_left']
        except:
            distance_tower_left = ''
        try:
            length_side_A_option_1 = request.POST['length_side_A_option_1']
        except:
            length_side_A_option_1 = ''
        try:
            length_side_B_option_1 = request.POST['length_side_B_option_1']
        except:
            length_side_B_option_1 = ''
        try:
            length_side_C_option_1 = request.POST['length_side_C_option_1']
        except:
            length_side_C_option_1 = ''
        try:
            length_side_D_option_1 = request.POST['length_side_D_option_1']
        except:
            length_side_D_option_1 = ''
        try:
            length_side_A_option_2 = request.POST['length_side_A_option_2']
        except:
            length_side_A_option_2 = ''
        try:
            length_side_B_option_2 = request.POST['length_side_B_option_2']
        except:
            length_side_B_option_2 = ''
        try:
            length_side_C_option_2 = request.POST['length_side_C_option_2']
        except:
            length_side_C_option_2 = ''
        try:
            length_side_D_option_2 = request.POST['length_side_D_option_2']
        except:
            length_side_D_option_2 = ''
        try:
            sketch_1 = request.FILES['sketch_1']
        except:
            sketch_1 = None
        try:
            sketch_2 = request.FILES['sketch_2']
        except:
            sketch_2 = None
        try:
            sketch_3 = request.FILES['sketch_3']
        except:
            sketch_3 = None
        try:
            sketch_4 = request.FILES['sketch_4']
        except:
            sketch_4 = None
        try:
            supportingImagesNumber = request.POST['supportingImagesNumber']
        except:
            supportingImagesNumber = ''
        try:
            status_stage = request.POST['status_stage']
            if not status_stage.isnumeric():
                raise Exception("Default")
        except:
            status_stage = '1'

        from django.core.files.storage import FileSystemStorage
        from PIL import Image
        from django.utils.timezone import make_aware
        from django.core.files import File

        try:
            SiteMaster.objects.create(site_id=site_id, site_name=site_name, site_region=site_region,
                                      site_latitude=site_latitude, site_longitude=site_longitude)
        except:
            pass
        try:
            ContractMaster.objects.create(
                contractor=contractor, contractor_rep=contractor_rep, contact_contractor_rep=contact_contractor_rep)
        except:
            pass
        details = None
        dcsupply = None
        dimension = None
        geography = None
        try:
            details = SiteDetails.objects.create(
                dc_system_on_site=bool(
                    int(dc_system_on_site)) if dc_system_on_site != None else dc_system_on_site,
                dc_system_brand=dc_system_brand, dc_system_size=dc_system_size,
                space_avail_in_dc_cabinet=bool(
                    int(space_avail_in_dc_cabinet)) if space_avail_in_dc_cabinet != None else space_avail_in_dc_cabinet,
                length_dc_cabinet=length_dc_cabinet if length_dc_cabinet != '' else None,
                height_dc_cabinet=height_dc_cabinet if height_dc_cabinet != '' else None,
                tall_structure=bool(
                    int(tall_structure)) if tall_structure != None else tall_structure,
                tall_structure_name=tall_structure_name,
                tall_structure_height=tall_structure_height if tall_structure_height != '' else None,
                tall_structure_distance_fence=tall_structure_distance_fence if tall_structure_distance_fence != '' else None,
                distance_shed_dc_cabinate=distance_shed_dc_cabinate if distance_shed_dc_cabinate != '' else None,
                comment=comment
            )
            dcsupply=DCSupplyParameter.objects.create(
                system_voltage=system_voltage if system_voltage != '' else None,
                load_current_1=load_current_1 if load_current_1 != '' else None,
                load_current_2=load_current_2 if load_current_2 != '' else None,
                load_current_3=load_current_3 if load_current_3 != '' else None,
                load_current_4=load_current_4 if load_current_4 != '' else None,
            )
            dimension=SiteDimensionDetails.objects.create(
                front_side=front_side if front_side != '' else None,
                right_side=right_side if right_side != '' else None,
                back_side=back_side if back_side != '' else None,
                left_side=left_side if left_side != '' else None,
                distance_tower_front=distance_tower_front if distance_tower_front != '' else None,
                distance_tower_right=distance_tower_right if distance_tower_right != '' else None,
                distance_tower_back=distance_tower_back if distance_tower_back != '' else None,
                distance_tower_left=distance_tower_left if distance_tower_left != '' else None,
                length_side_A_option_1=length_side_A_option_1 if length_side_A_option_1 != '' else None,
                length_side_B_option_1=length_side_B_option_1 if length_side_B_option_1 != '' else None,
                length_side_C_option_1=length_side_C_option_1 if length_side_C_option_1 != '' else None,
                length_side_D_option_1=length_side_D_option_1 if length_side_D_option_1 != '' else None,
                length_side_A_option_2=length_side_A_option_2 if length_side_A_option_2 != '' else None,
                length_side_B_option_2=length_side_B_option_2 if length_side_B_option_2 != '' else None,
                length_side_C_option_2=length_side_C_option_2 if length_side_C_option_2 != '' else None,
                length_side_D_option_2=length_side_D_option_2 if length_side_D_option_2 != '' else None
            )

            fs=FileSystemStorage()

            geography=GeographicalDetails()

            if sketch_1 != None:
                sketch_1=fs.save(sketch_1.name, sketch_1)
                try:
                    Image.open(settings.MEDIA_ROOT + '/' + sketch_1).verify()
                    geography.sketch_1.save(sketch_1, File(open(settings.MEDIA_ROOT + '/' + sketch_1, 'rb')))
                except Exception as ex:
                    print(ex)
                    os.remove(settings.MEDIA_ROOT + '/' + sketch_1)
                    raise Exception("Broken File")

            if sketch_2 != None:
                sketch_2=fs.save(sketch_2.name, sketch_2)
                try:
                    Image.open(settings.MEDIA_ROOT + '/' + sketch_2).verify()
                    geography.sketch_2.save(sketch_2, File(open(settings.MEDIA_ROOT + '/' + sketch_2, 'rb')))
                except Exception as ex:
                    print(ex)
                    os.remove(settings.MEDIA_ROOT + '/' + sketch_2)
                    raise Exception("Broken File")
            
            if sketch_3 != None:
                sketch_3=fs.save(sketch_3.name, sketch_3)
                try:
                    Image.open(settings.MEDIA_ROOT + '/' + sketch_3).verify()
                    geography.sketch_3.save(sketch_3, File(open(settings.MEDIA_ROOT + '/' + sketch_3, 'rb')))
                except Exception as ex:
                    print(ex)
                    os.remove(settings.MEDIA_ROOT + '/' + sketch_3)
                    raise Exception("Broken File")

            if sketch_4 != None:
                sketch_4=fs.save(sketch_4.name, sketch_4)
                try:
                    Image.open(settings.MEDIA_ROOT + '/' + sketch_4).verify()
                    geography.sketch_4.save(sketch_4, File(open(settings.MEDIA_ROOT + '/' + sketch_4, 'rb')))
                except Exception as ex:
                    print(ex)
                    os.remove(settings.MEDIA_ROOT + '/' + sketch_4)
                    raise Exception("Broken File")
            
            geography.save()
            
            for i in range(1, int(supportingImagesNumber) + 1):
                supportimgobj=SupportingImagesGeographical(geographicaldetails = geography)
                imagename=request.FILES['supporting_images_' + str(i)]
                imagename=fs.save(imagename.name, imagename)
                try:
                    Image.open(settings.MEDIA_ROOT + '/' + imagename).verify()
                    supportimgobj.supporting_images.save(imagename, File(open(settings.MEDIA_ROOT + '/' + imagename, 'rb')))
                    supportimgobj.supporting_images_caption = request.POST["supporting_images_caption" + "_" + str(i)]
                    supportimgobj.save()
                except Exception as ex:
                    print(ex)
                    os.remove(settings.MEDIA_ROOT + '/' + imagename)
                    raise Exception("Broken File")
        except Exception as ex:
            print(ex)
            if details != None:
                details.delete()
                details=None
            if dcsupply != None:
                dcsupply.delete()
                dcsupply=None
            if dimension != None:
                dimension.delete()
                dimension=None
            if geography != None:
                geography.delete()
                geography=None
        try:
            site=SiteMaster.objects.get(site_id=site_id)
            contract=ContractMaster.objects.get(
                contractor=contractor, contractor_rep=contractor_rep, contact_contractor_rep=contact_contractor_rep)
            SiteVisit.objects.create(site=site, contract=contract, details=details,
                                     dcsupply=dcsupply, dimension=dimension, geography=geography,
                                     visited=make_aware(
                                         datetime.datetime.strptime(
                                             visited_date + " " + visited_time, "%Y-%m-%d %H:%M"
                                             )), status_stage=int(status_stage))
        except Exception as ex:
            print(ex)
            return render(request, 'frontend/tss-entry.html', {"activepage": "tssentry", "error": str(ex)})
        return redirect('/tss-view')
    return render(request, 'frontend/tss-entry.html', {"activepage": "tssentry"})















def tssEdit(request):
    data = {}
    sitevisit = SiteVisit.objects.get(id=request.GET.get('id'))
    if request.method == 'POST':
        try:
            dc_system_on_site = request.POST['dc_system_on_site']
        except:
            dc_system_on_site = ''
        try:
            dc_system_brand = request.POST['dc_system_brand']
        except:
            dc_system_brand = ''
        try:
            dc_system_size = request.POST['dc_system_size']
        except:
            dc_system_size = ''
        try:
            space_avail_in_dc_cabinet = request.POST['space_avail_in_dc_cabinet']
        except:
            space_avail_in_dc_cabinet = ''
        try:
            length_dc_cabinet = request.POST['length_dc_cabinet']
        except:
            length_dc_cabinet = ''
        try:
            height_dc_cabinet = request.POST['height_dc_cabinet']
        except:
            height_dc_cabinet = ''
        try:
            tall_structure = request.POST['tall_structure']
        except:
            tall_structure = ''
        try:
            tall_structure_name = request.POST['tall_structure_name']
        except:
            tall_structure_name = ''
        try:
            tall_structure_height = request.POST['tall_structure_height']
        except:
            tall_structure_height = ''
        try:
            tall_structure_distance_fence = request.POST['tall_structure_distance_fence']
        except:
            tall_structure_distance_fence = ''
        try:
            distance_shed_dc_cabinate = request.POST['distance_shed_dc_cabinate']
        except:
            distance_shed_dc_cabinate = ''
        try:
            comment = request.POST['comment']
        except:
            comment = ''
        try:
            system_voltage = request.POST['system_voltage']
        except:
            system_voltage = ''
        try:
            load_current_1 = request.POST['load_current_1']
        except:
            load_current_1 = ''
        try:
            load_current_2 = request.POST['load_current_2']
        except:
            load_current_2 = ''
        try:
            load_current_3 = request.POST['load_current_3']
        except:
            load_current_3 = ''
        try:
            load_current_4 = request.POST['load_current_4']
        except:
            load_current_4 = ''
        try:
            front_side = request.POST['front_side']
        except:
            front_side = ''
        try:
            right_side = request.POST['right_side']
        except:
            right_side = ''
        try:
            back_side = request.POST['back_side']
        except:
            back_side = ''
        try:
            left_side = request.POST['left_side']
        except:
            left_side = ''
        try:
            distance_tower_front = request.POST['distance_tower_front']
        except:
            distance_tower_front = ''
        try:
            distance_tower_right = request.POST['distance_tower_right']
        except:
            distance_tower_right = ''
        try:
            distance_tower_back = request.POST['distance_tower_back']
        except:
            distance_tower_back = ''
        try:
            distance_tower_left = request.POST['distance_tower_left']
        except:
            distance_tower_left = ''
        try:
            length_side_A_option_1 = request.POST['length_side_A_option_1']
        except:
            length_side_A_option_1 = ''
        try:
            length_side_B_option_1 = request.POST['length_side_B_option_1']
        except:
            length_side_B_option_1 = ''
        try:
            length_side_C_option_1 = request.POST['length_side_C_option_1']
        except:
            length_side_C_option_1 = ''
        try:
            length_side_D_option_1 = request.POST['length_side_D_option_1']
        except:
            length_side_D_option_1 = ''
        try:
            length_side_A_option_2 = request.POST['length_side_A_option_2']
        except:
            length_side_A_option_2 = ''
        try:
            length_side_B_option_2 = request.POST['length_side_B_option_2']
        except:
            length_side_B_option_2 = ''
        try:
            length_side_C_option_2 = request.POST['length_side_C_option_2']
        except:
            length_side_C_option_2 = ''
        try:
            length_side_D_option_2 = request.POST['length_side_D_option_2']
        except:
            length_side_D_option_2 = ''
        try:
            sketch_1 = request.FILES['sketch_1']
        except:
            sketch_1 = None
        try:
            sketch_2 = request.FILES['sketch_2']
        except:
            sketch_2 = None
        try:
            sketch_3 = request.FILES['sketch_3']
        except:
            sketch_3 = None
        try:
            sketch_4 = request.FILES['sketch_4']
        except:
            sketch_4 = None
        try:
            supportingImagesNumber = request.POST['supportingImagesNumber']
        except:
            supportingImagesNumber = ''
        try:
            status_stage = request.POST['status_stage']
            if not status_stage.isnumeric():
                raise Exception("Default")
        except:
            status_stage = '1'

        from django.core.files.storage import FileSystemStorage
        from PIL import Image
        from django.utils.timezone import make_aware
        from django.core.files import File

        details = sitevisit.details
        dcsupply = sitevisit.dcsupply
        dimension = sitevisit.dimension
        geography = sitevisit.geography
        
        try:
            details.dc_system_on_site=bool(int(dc_system_on_site)) if dc_system_on_site != None else dc_system_on_site
            details.dc_system_brand=dc_system_brand 
            details.dc_system_size=dc_system_size
            details.space_avail_in_dc_cabinet=bool(int(space_avail_in_dc_cabinet)) if space_avail_in_dc_cabinet != None else space_avail_in_dc_cabinet
            details.length_dc_cabinet=length_dc_cabinet if length_dc_cabinet != '' else None
            details.height_dc_cabinet=height_dc_cabinet if height_dc_cabinet != '' else None
            details.tall_structure=bool(int(tall_structure)) if tall_structure != None else tall_structure
            details.tall_structure_name=tall_structure_name
            details.tall_structure_height=tall_structure_height if tall_structure_height != '' else None
            details.tall_structure_distance_fence=tall_structure_distance_fence if tall_structure_distance_fence != '' else None
            details.distance_shed_dc_cabinate=distance_shed_dc_cabinate if distance_shed_dc_cabinate != '' else None
            details.comment=comment
            details.save()

            dcsupply.system_voltage=system_voltage if system_voltage != '' else None
            dcsupply.load_current_1=load_current_1 if load_current_1 != '' else None
            dcsupply.load_current_2=load_current_2 if load_current_2 != '' else None
            dcsupply.load_current_3=load_current_3 if load_current_3 != '' else None
            dcsupply.load_current_4=load_current_4 if load_current_4 != '' else None
            dcsupply.save()

            
            dimension.front_side=front_side if front_side != '' else None
            dimension.right_side=right_side if right_side != '' else None
            dimension.back_side=back_side if back_side != '' else None
            dimension.left_side=left_side if left_side != '' else None
            dimension.distance_tower_front=distance_tower_front if distance_tower_front != '' else None
            dimension.distance_tower_right=distance_tower_right if distance_tower_right != '' else None
            dimension.distance_tower_back=distance_tower_back if distance_tower_back != '' else None
            dimension.distance_tower_left=distance_tower_left if distance_tower_left != '' else None
            dimension.length_side_A_option_1=length_side_A_option_1 if length_side_A_option_1 != '' else None
            dimension.length_side_B_option_1=length_side_B_option_1 if length_side_B_option_1 != '' else None
            dimension.length_side_C_option_1=length_side_C_option_1 if length_side_C_option_1 != '' else None
            dimension.length_side_D_option_1=length_side_D_option_1 if length_side_D_option_1 != '' else None
            dimension.length_side_A_option_2=length_side_A_option_2 if length_side_A_option_2 != '' else None
            dimension.length_side_B_option_2=length_side_B_option_2 if length_side_B_option_2 != '' else None
            dimension.length_side_C_option_2=length_side_C_option_2 if length_side_C_option_2 != '' else None
            dimension.length_side_D_option_2=length_side_D_option_2 if length_side_D_option_2 != '' else None
            dimension.save()

            fs=FileSystemStorage()

            if sketch_1 != None:
                sketch_1=fs.save(sketch_1.name, sketch_1)
                try:
                    Image.open(settings.MEDIA_ROOT + '/' + sketch_1).verify()
                    geography.sketch_1.save(sketch_1, File(open(settings.MEDIA_ROOT + '/' + sketch_1, 'rb')))
                except Exception as ex:
                    print(ex)
                    os.remove(settings.MEDIA_ROOT + '/' + sketch_1)
                    raise Exception("Broken File")

            if sketch_2 != None:
                sketch_2=fs.save(sketch_2.name, sketch_2)
                try:
                    Image.open(settings.MEDIA_ROOT + '/' + sketch_2).verify()
                    geography.sketch_2.save(sketch_2, File(open(settings.MEDIA_ROOT + '/' + sketch_2, 'rb')))
                except Exception as ex:
                    print(ex)
                    os.remove(settings.MEDIA_ROOT + '/' + sketch_2)
                    raise Exception("Broken File")
            
            if sketch_3 != None:
                sketch_3=fs.save(sketch_3.name, sketch_3)
                try:
                    Image.open(settings.MEDIA_ROOT + '/' + sketch_3).verify()
                    geography.sketch_3.save(sketch_3, File(open(settings.MEDIA_ROOT + '/' + sketch_3, 'rb')))
                except Exception as ex:
                    print(ex)
                    os.remove(settings.MEDIA_ROOT + '/' + sketch_3)
                    raise Exception("Broken File")

            if sketch_4 != None:
                sketch_4=fs.save(sketch_4.name, sketch_4)
                try:
                    Image.open(settings.MEDIA_ROOT + '/' + sketch_4).verify()
                    geography.sketch_4.save(sketch_4, File(open(settings.MEDIA_ROOT + '/' + sketch_4, 'rb')))
                except Exception as ex:
                    print(ex)
                    os.remove(settings.MEDIA_ROOT + '/' + sketch_4)
                    raise Exception("Broken File")
            
            geography.save()
            
            supportimglist=SupportingImagesGeographical.objects.filter(geographicaldetails = geography)
            for i in range(1, int(supportingImagesNumber) + 1):
                try:
                    supportimgobj=supportimglist[i - 1]
                except:
                    supportimgobj=SupportingImagesGeographical(geographicaldetails = geography)    
                try:
                    imagename=request.FILES['supporting_images_' + str(i)]
                except:
                    imagename = None
                if imagename != None:
                    imagename=fs.save(imagename.name, imagename)
                    try:
                        Image.open(settings.MEDIA_ROOT + '/' + imagename).verify()
                        supportimgobj.supporting_images.save(imagename, File(open(settings.MEDIA_ROOT + '/' + imagename, 'rb')))
                        try:
                            supportimgobj.supporting_images_caption = request.POST["supporting_images_caption" + "_" + str(i)]
                        except:
                            supportimgobj.supporting_images_caption = ''
                        supportimgobj.save()
                    except Exception as ex:
                        print(ex)
                        os.remove(settings.MEDIA_ROOT + '/' + imagename)
                        raise Exception("Broken File")
            if supportimglist.count() > int(supportingImagesNumber):
                for i in range(int(supportingImagesNumber) - 1, supportimglist.count()):        
                    try:
                        supportimglist[i].delete()
                    except:
                        pass
            sitevisit.status_stage=int(status_stage)
            sitevisit.save()
            data["error"] = "Updated"
        except Exception as ex:
            print(ex)
            data["error"] = str(ex)
        
    data["sitevisit"] =  sitevisit
    extra_imgs = SupportingImagesGeographical.objects.filter(geographicaldetails=sitevisit.geography)
    data["extra_imgs"] = extra_imgs if extra_imgs.count() > 0 else None
        
    return render(request, 'frontend/tss-edit.html', data)