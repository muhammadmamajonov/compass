from dashboard.models import Fan, Oqituvchi, Talaba
from django.contrib import messages
from django.shortcuts import render
from django.http import JsonResponse
import json

from .models import *


# Create your views here.

def index(request):
    if request.method == 'POST':
        ism = request.POST['ism']
        tel = request.POST['telefon']
        toliq = request.POST['malumot']
        dars = request.POST.getlist('fan')
        manzil = request.POST['manzil']
        qayerdan_keldi = request.POST['qayerdan_keldi']
        
        lead = MalumotQoldirish.objects.create(ism=ism, telefon=tel, toliq=toliq, manzil=manzil)
        for fan in dars:
            fan = Fan.objects.get(id=fan)
            lead.dars.add(fan)
            
            
       
        messages.info(request, "Murojatingiz qabul qilindi, tez orada siz bilan bog'lanamiz")
    oqituvchilar_soni = Oqituvchi.objects.all().count()
    talabalar_soni = Talaba.objects.all().count
    fanlar = Fan.objects.all()
    fanlar_soni = fanlar.count
    gallery = Galareya.objects.all()
    oqituvchilar = Oqituvchi.objects.all()
    oquvchilar_soni = Talaba.objects.all().count()
    events = Events.objects.all()
    malumotlar1 = malumot.objects.all()[0:2]
    malumotlar2 = malumot.objects.all()[2:]
    slider = Slider.objects.order_by('-id')[0:3]
    haqimizda = Haqimizda.objects.first()
    tarmoqlar = Tarmoq.objects.all()
    contact = Contact.objects.first()
    izoxlar = Bolim_izox.objects.first()
    bitirganlar = Bitirganlar.objects.first()
    slider1 = ''
    slider2 = ''
    slider3 = ''
    i = 0
    for slide in slider:
        if i == 0:
            i += 1
            slider1 = slide
        elif i == 1:
            slider2 = slide
            i += 1
        else:
            slider3 = slide

    return render(request, 'index.html',
                  {'malumotlar1': malumotlar1, 'malumotlar2': malumotlar2, 'slider1': slider1, 'slider2': slider2,
                   'slider3': slider3, 'events': events, 'oquvchilar_soni': oquvchilar_soni, 'bitirganlar':bitirganlar,
                   'oqituchilar_soni': oqituvchilar_soni, 'oqituvchilar': oqituvchilar, 'gallery': gallery, 'izoxlar':izoxlar,
                   'fanlar': fanlar, 'fanlar_soni': fanlar_soni, 'talabalar_soni': talabalar_soni, 'haqimizda':haqimizda, "tarmoqlar":tarmoqlar, 'contact':contact})

