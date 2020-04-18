from django.urls import path

from . import views

urlpatterns = [
    path('', views.loginSmart, name='loginSmart'),
    path('logout', views.logOutSmart, name='logOutSmart'),
    path('index', views.indexSmart, name='indexSmart'),
    path('blank', views.blankSmart, name='blankSmart'),
    path('tss-entry', views.tssEntrySmart, name='tssEntrySmart'),
    path('tss-view', views.tssViewSmart, name='tssviewSmart'),
    path('tss-view-pdf', views.tssViewSmartPDF, name='tssViewSmartPDF'),
]