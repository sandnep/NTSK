
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from soapsystem.forms import inform
from .models import *

installed_apps = ['soapsystem']

def Mainpage(request):
	return render(request,'soapsystem/mainpage.html')

def Aboutshop(request):
	return render(request,'soapsystem/aboutshop.html')

def Soaps(request):
	return render(request,'soapsystem/soaps.html')
def kojicbenefits(request):
	return render(request,'soapsystem/kojicbenefits.html')

def glassbenefits(request):
	return render(request,'soapsystem/glassbenefits.html')

def glutabenefits(request):
	return render(request,'soapsystem/glutabenefits.html')
def oatbenefits(request):
	return render(request,'soapsystem/oatbenefits.html')

def charbenefits(request):
	return render(request,'soapsystem/charbenefits.html')

def Records(request):
	informations = information.objects.all()
	ContactForms = ContactForm.objects.all()
	Feedbacks = Feedback.objects.all()
	return render(request,'soapsystem/Records.html', {'information':informations, 'ContactForm':ContactForms, 'Feedback':Feedbacks})

def SoapBuy(request):
	if request.method == "POST":
		lastname = request.POST['lastname']
		firstname = request.POST['firstname']
		middlename = request.POST['middlename']
		contact = request.POST['contact']
		email = request.POST['email']
		street = request.POST['street']
		subd = request.POST['subd']
		brgy = request.POST['brgy']
		city = request.POST['city']
		zipcode = request.POST['zipcode']
		soapname = request.POST['soapname']
		qty = request.POST['qty']
		inf = information.objects.create(lastname = lastname, firstname = firstname,
		middlename = middlename, 
		contact = contact, 
		email = email,
		street = street,
		subd = subd,
		brgy = brgy,
		city = city,
		zipcode = zipcode, 
		soapname = soapname, 
		qty = qty
		)
		inf.save()
	return render(request,'soapsystem/Soapbuy.html')


def contactform(request):
	if request.method == "POST":
		name = request.POST['name']
		email = request.POST['email']
		message = request.POST['message']
		cont = ContactForm.objects.create(name = name, email = email, message = message)
		cont.save()
	return render(request,'soapsystem/contactform.html')

def feedback(request):
	if request.method == "POST":
		message = request.POST['message']
		fdb = Feedback.objects.create( message = message)
		fdb.save()		
	return render(request,'soapsystem/feedback.html')

def Edit(request, id):
	data = information.objects.get(id=id)
	form = inform(instance=data)
	if request.method == 'POST':
		form = inform(request.POST, instance = data)
		if form.is_valid():
			form.save()
			return redirect('/Records')

	return render(request, 'soapsystem/update.html', {'form':form})

		
def Cancel(request, id):
    canc = information.objects.get(id=id)
    for x in information.objects.only('id'):
        if canc == x:
            x = information.objects.get(id=id).delete()
            break
    return redirect('/Records')

def Cancel1(request, id):
    canc = ContactForm.objects.get(id=id)
    for x in ContactForm.objects.only('id'):
        if canc == x:
            x = ContactForm.objects.get(id=id).delete()
            break
    return redirect('/Records')

def Cancel2(request, id):
    canc = Feedback.objects.get(id=id)
    for x in Feedback.objects.only('id'):
        if canc == x:
            x = Feedback.objects.get(id=id).delete()
            break
    return redirect('/Records')
