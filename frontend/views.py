from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.defaults import bad_request

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

from api.models import *
from django.conf import settings
import os

import datetime


# Create your views here.


#Login
@csrf_protect
def loginSmart(request):
    from django.contrib.auth import authenticate, login
    wrongUser = {}
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
        except Exception as ex:
            return bad_request(request, ex)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                wrongUser = {"message": "Please use Site Admin"}
            else:
                try:
                    CompanyUser.objects.get(user=user).comp
                    login(request, user)
                except:
                    wrongUser = {"message": "Please contact admin to assign your company and your role. Then you can login"}
        else:
            wrongUser = {"message": "Wrong username or password"}
    if request.user.is_authenticated:
        return redirect('/index')
    return render(request, 'frontend/login.html', wrongUser)


#DashBoard
@login_required(login_url='/')
def indexSmart(request):
    return render(request, 'frontend/index.html', {"activepage": "index"})



#Unnecessary
@login_required(login_url='/')
def blankSmart(request):
    return render(request, 'frontend/blank.html')



#TSS view Table Here we can also change TSS Stage Status
@login_required(login_url='/')
def tssViewSmart(request):
    try:
        if not request.user.is_superuser:
            comp = CompanyUser.objects.get(user=request.user).comp
            if comp == 'ATC':
                stat = 9
            elif comp in ['VYOMA', 'PARK']:
                stat = 0
            else:
                raise Exception("Bad company")
        else:
            stat = 0
        return render(request, 'frontend/tss-view.html', {"sitevisit": SiteVisit.objects.filter(status_stage__gte=stat)})
    except Exception as ex:
        return bad_request(request, ex)




#TSS PDF 
@login_required(login_url='/')
def tssViewSmartPDF(request):
    try:
        sitevisitobj = SiteVisit.objects.get(id=request.GET.get('id'))
        return render(request, 'frontend/pdf_template.html', {
            "sitevisit": sitevisitobj,
            "extra_imgs": SupportingImagesGeographical.objects.filter(geographicaldetails=sitevisitobj.geography),
        })
    except Exception as ex:
        print(ex)
        return bad_request(request, ex)




#Site Distribution according to Company users
@csrf_protect
@login_required(login_url='/')
def tssAssign(request):
    try:
        task = request.GET.get('task')
        if task not in ['Layout Drawing', 'Solar Analysis', 'TSS Entry']:
            raise Exception("Wrong Task")
        if request.method == 'POST':
            site_visit = request.POST['site_visit']
            assigned = request.POST['assigned']
            comment = request.POST['comment']
            assu = User.objects.get(username=assigned)
            # print(site_visit)
            # print(assigned)
            # print(comment)
            # print(assu)
            CompanyUser.objects.get(user=assu).role
            if assu.is_superuser:
                raise Exception("Bad role")
            AssignUser.objects.create(
                site_visit = SiteVisit.objects.get(id=site_visit),
                assigned = assu,
                task=task,
                comment = comment
            )
        data = {
            "assignuser": AssignUser.objects.filter(task=task), 
            "sitevisit": SiteVisit.objects.all(),
            "task": task,
            "companyuser": CompanyUser.objects.filter(),
        }
        if request.user.is_superuser:
            data["perm"] = 'ASSIGN'
        else:
            data["perm"] = CompanyUser.objects.get(user=request.user).role
        return render(request, 'frontend/tss-assign.html', data)
    except Exception as ex:
        print(ex)
        return bad_request(request, ex)



#TSS Entry as discussed previously
@csrf_protect
@login_required(login_url='/')
def tssEntrySmart(request):
    from .supportview.tssIUview import tssEntry
    try:
        return tssEntry(request)
    except Exception as ex:
        print(ex)
        return bad_request(request, ex)





#TSS Edit By helper function
@csrf_protect
@login_required(login_url='/')
def tssUpdateSmart(request):
    from .supportview.tssIUview import tssEdit
    try:
        return tssEdit(request)
    except Exception as ex:
        print(ex)
        return bad_request(request, ex)



#BY SHANTANU (MEANINGLESS till now because there is no link mapping)
@login_required(login_url='/')
def siteSetup(request):
    try:
        return render(request, 'frontend/site_setup.html')
    except Exception as ex:
        print(ex)
        return bad_request(request, ex)


#Site Entry AJAX CALL In Site Setup (Incomplete)
@login_required(login_url='/')
def siteSetupSiteEntry(request): 
    try:
        if request.method == 'POST':
            # from django.http import JsonResponse
            #Code to Create SiteVisit Object with foreign Key SiteMaster
            #return JsonResponse with SiteVisit Object & status 200
            return HttpResponse(status=200)
    except Exception as ex:
        print(ex)
        return HttpResponse(status=400)





#TSS status Stage updatevia AJAX call with get method
@login_required(login_url='/')
def tssStatusUpdateSmart(request):
    try:
        status_stage=int(request.GET.get('status_stage'))
        visit_id=request.GET.get('visit_id')
        print(status_stage)
        print(visit_id)
        if not (1 <= status_stage and status_stage <= 8):
            raise Exception("Bad Status Stage")
        sitevisitobj = SiteVisit.objects.get(id=visit_id)
        sitevisitobj.status_stage = int(status_stage)
        sitevisitobj.save()
        return HttpResponse(status=200)
    except Exception as ex:
        print(ex)
        return HttpResponse(status=400)





#Logout from Site for non admin users
@login_required(login_url='/')
def logOutSmart(request):
    from django.contrib.auth import logout
    try:
        if request.user.is_superuser:
            return redirect('/admin')
        logout(request)
        return redirect('/')
    except Exception as ex:
        print(ex)
        return bad_request(request, ex)
