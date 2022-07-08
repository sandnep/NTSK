from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('',views.Mainpage, name='Mainpage'),
    path('Aboutshop/',views.Aboutshop, name='Aboutshop'),
    path('Soaps/',views.Soaps, name='Soaps'),
    path('SoapBuy/',views.SoapBuy, name='SoapBuy'),
    path('contactform/',views.contactform, name='contactform'), 
    path('feedback/',views.feedback, name='feedback'),
    path('Records/',views.Records, name='Records'),
    path('Cancel/<int:id>', views.Cancel, name='Cancel'),
    path('Cancel1/<int:id>', views.Cancel1, name='Cancel1'),
    path('Cancel2/<int:id>', views.Cancel2, name='Cancel2'),
    path('Edit/<int:id>', views.Edit, name='Edit'),
    path('kojicbenefits/',views.kojicbenefits, name='kojicbenefits'),
    path('glassbenefits/',views.glassbenefits, name='glassbenefits'),
    path('glutabenefits/',views.glutabenefits, name='glutabenefits'), 
    path('oatbenefits/',views.oatbenefits, name='oatbenefits'),
    path('charbenefits/',views.charbenefits, name='charbenefits'),
    ]