from django.shortcuts import render, redirect
from django.http import HttpResponse

from api.models import *
from django.conf import settings
import os

import datetime


# Create your views here.


def loginSmart(request):
    if request.method == 'POST':
        return redirect('/index')
    return render(request, 'frontend/login.html')


def indexSmart(request):
    return render(request, 'frontend/index.html', {"activepage": "index"})


def blankSmart(request):
    return render(request, 'frontend/blank.html')


def tssViewSmart(request):
    return render(request, 'frontend/tss-view.html', {"sitevisit": SiteVisit.objects.all()})



def tssViewSmartPDF(request):
    try:
        pass
        sitevisitobj = SiteVisit.objects.get(id=request.GET.get('id'))

        from io import BytesIO
        from django.template.loader import get_template
        from xhtml2pdf import pisa

        def link_callback(uri, rel):
            sUrl = settings.STATIC_URL      # Typically /static/
            sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
            mUrl = settings.MEDIA_URL       # Typically /static/media/
            mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/
            # convert URIs to absolute system paths
            if uri.startswith(mUrl):
                path = os.path.join(mRoot, uri.replace(mUrl, ""))
            elif uri.startswith(sUrl):
                path = os.path.join(sRoot, uri.replace(sUrl, ""))
            else:
                return uri  # handle absolute uri (ie: http://some.tld/foo.png)
            # make sure that file exists
            if not os.path.isfile(path):
                    raise Exception(
                        'media URI must start with %s or %s' % (sUrl, mUrl)
                    )
            return path

        template = get_template('frontend/pdf_template.html')
        html  = template.render({
            "sitevisit": sitevisitobj,
            "extra_imgs":SupportingImagesGeographical.objects.filter(geographicaldetails=sitevisitobj.geography),
        })
        result = BytesIO()
        try:
            pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result, link_callback=link_callback)
            pdf = HttpResponse(result.getvalue(), content_type='application/pdf')
        except:
            pdf = None
        
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "TSS_Report_"+ str(sitevisitobj.site.site_id) + str(sitevisitobj.visited.strftime("%d_%m_%Y")) +".pdf"
        content = "attachment; filename="+(filename)
        response['Content-Disposition'] = content
        return response
    except Exception as ex:
        print(ex)
        from django.views.defaults import bad_request
        return bad_request(request, ex)



def tssEntrySmart(request):
    if request.method == 'POST':
        site_id = request.POST['site_id']
        site_name = request.POST['site_name']
        visited_date = request.POST['visited_date']
        visited_time = request.POST['visited_time']
        site_region = request.POST['site_region']
        site_latitude = request.POST['site_latitude']
        site_longitude = request.POST['site_longitude']
        contractor = request.POST['contractor']
        contractor_rep = request.POST['contractor_rep']
        contact_contractor_rep = request.POST['contact_contractor_rep']
        dc_system_on_site = request.POST['dc_system_on_site']
        dc_system_brand = request.POST['dc_system_brand']
        dc_system_size = request.POST['dc_system_size']
        space_avail_in_dc_cabinet = request.POST['space_avail_in_dc_cabinet']
        length_dc_cabinet = request.POST['length_dc_cabinet']
        height_dc_cabinet = request.POST['height_dc_cabinet']
        tall_structure = request.POST['tall_structure']
        tall_structure_name = request.POST['tall_structure_name']
        tall_structure_height = request.POST['tall_structure_height']
        tall_structure_distance_fence = request.POST['tall_structure_distance_fence']
        distance_shed_dc_cabinate = request.POST['distance_shed_dc_cabinate']
        comment = request.POST['comment']
        system_voltage = request.POST['system_voltage']
        load_current_1 = request.POST['load_current_1']
        load_current_2 = request.POST['load_current_2']
        load_current_3 = request.POST['load_current_3']
        load_current_4 = request.POST['load_current_4']
        front_side = request.POST['front_side']
        right_side = request.POST['right_side']
        back_side = request.POST['back_side']
        left_side = request.POST['left_side']
        distance_tower_front = request.POST['distance_tower_front']
        distance_tower_right = request.POST['distance_tower_right']
        distance_tower_back = request.POST['distance_tower_back']
        distance_tower_left = request.POST['distance_tower_left']
        length_side_A_option_1 = request.POST['length_side_A_option_1']
        length_side_B_option_1 = request.POST['length_side_B_option_1']
        length_side_C_option_1 = request.POST['length_side_C_option_1']
        length_side_D_option_1 = request.POST['length_side_D_option_1']
        length_side_A_option_2 = request.POST['length_side_A_option_2']
        length_side_B_option_2 = request.POST['length_side_B_option_2']
        length_side_C_option_2 = request.POST['length_side_C_option_2']
        length_side_D_option_2 = request.POST['length_side_D_option_2']
        sketch_1 = request.FILES['sketch_1']
        sketch_2 = request.FILES['sketch_2']
        sketch_3 = request.FILES['sketch_3']
        sketch_4 = request.FILES['sketch_4']
        supportingImagesNumber = request.POST['supportingImagesNumber']

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

            sketch_1=fs.save(sketch_1.name, sketch_1)
            try:
                Image.open(settings.MEDIA_ROOT + '/' + sketch_1).verify()
                geography.sketch_1.save(sketch_1, File(open(settings.MEDIA_ROOT + '/' + sketch_1, 'rb')))
            except Exception as ex:
                print(ex)
                os.remove(settings.MEDIA_ROOT + '/' + sketch_1)
                raise Exception("Broken File")

            sketch_2=fs.save(sketch_2.name, sketch_2)
            try:
                Image.open(settings.MEDIA_ROOT + '/' + sketch_2).verify()
                geography.sketch_2.save(sketch_2, File(open(settings.MEDIA_ROOT + '/' + sketch_2, 'rb')))
            except Exception as ex:
                print(ex)
                os.remove(settings.MEDIA_ROOT + '/' + sketch_2)
                raise Exception("Broken File")

            sketch_3=fs.save(sketch_3.name, sketch_3)
            try:
                Image.open(settings.MEDIA_ROOT + '/' + sketch_3).verify()
                geography.sketch_3.save(sketch_3, File(open(settings.MEDIA_ROOT + '/' + sketch_3, 'rb')))
            except Exception as ex:
                print(ex)
                os.remove(settings.MEDIA_ROOT + '/' + sketch_3)
                raise Exception("Broken File")

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
                                     visited=make_aware(datetime.datetime.strptime(visited_date + " " + visited_time, "%Y-%m-%d %H:%M")))
        except Exception as ex:
            print(ex)
            return render(request, 'frontend/tss-entry.html', {"activepage": "tssentry", "error": str(ex)})
        return redirect('/tss-view')
    return render(request, 'frontend/tss-entry.html', {"activepage": "tssentry"})


def logOutSmart(request):
    return redirect('/')
