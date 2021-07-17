from django.shortcuts import render, redirect
from public.models import MalumotQoldirish
from .models import *
from django.views.generic import DetailView
from django.http import JsonResponse
import json
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user, logout, login, authenticate
from datetime import datetime, timedelta


# Create your views here.

def Chart(request):
    tol = []
    tal = []
    for i in range(1, 13):
        date = datetime.today()
        year = date.year
        if i == 12:
            month2 = 1
            year2 = year + 1
        else:
            month2 = i + 1
            year2 = year
        gte1 = datetime(year, i, 1)
        lte1 = datetime(year2, month2, 1)
        tolov = Tolov.objects.filter(sana__gte=gte1, sana__lt=lte1).count()
        talaba = Talaba.objects.filter(sana__gte=gte1, sana__lt=lte1).count()
        tol.append(tolov)
        tal.append(talaba)
    dt = {
        'tolov': tol,
        'talaba': tal,
    }
    t = Talaba.objects.all()
    return JsonResponse(dt)


#################### INDEX #############################################


#################### Admin Dashboard #############################################
def guruh_tolamaganlar(request):
    if request.method == "GET":
        print("shu yerda")
        grid = request.GET.get('i')
        print(grid)
        g = Guruh.objects.get(id=grid)
        tolovlar = Tolov.objects.filter(oy_id=datetime.now().month)
        guruh_talabalari = g.azolik_set.all()

        tolamaganlar = []
        tolaganlar = []
        tolaganlar_id = []
        dt = []
        print("13-id dagi talaba:")
        for t in tolovlar:
            tolaganlar_id.append(t.id)

        if tolovlar:
            for talaba in guruh_talabalari:
                print(talaba.talaba.id, ":", t.talaba_ism.id)
                if talaba.talaba.id not in tolaganlar_id:
                    print(talaba.talaba.ism_familya)
                    data = {
                        'ism_familya': talaba.talaba.ism_familya,
                        'id': talaba.talaba.id
                    }
                    dt.append(data)
                    print("data", data, "dt", dt)
                    print("tolaganlar id:", tolaganlar_id)
        else:
            print(guruh_talabalari)
            for gt in guruh_talabalari:
                print(gt)
                data = {
                    'id': gt.talaba.id,
                    'ism_familya': gt.talaba.ism_familya
                }
                dt.append(data)
        # dt.append(data)
        return JsonResponse({'dt': dt}, safe=False)
    return render(request, 'index.html')


def AdminDash(request):
    user = get_user(request)
    if user.is_authenticated:
        if user.is_staff:
            if request.method == 'POST':
                k_id = request.POST['kutayotgan_id']
                k = Kutayotganlar.objects.get(id=k_id)
                Talaba.objects.create(ism_familya=k.ism_familya, dars=k.dars, telefon=k.telefon, manzil=k.manzil)
                k.delete()
                return redirect('/dashboard')
            oqituvchilar = Oqituvchi.objects.all()
            talabalar = Talaba.objects.all()
            talabalar_1_foiz = talabalar.count() / 100
            fanlar = Fan.objects.filter(status=1)
            kutayotganlar = Kutayotganlar.objects.all().order_by('id')[:7]
            tolovlar = Tolov.objects.filter(oy_id=datetime.now().month)
            barchaOquvchi = Azolik.objects.all().count()
            pul_shu_oy = 0
            for t in tolovlar:
                pul_shu_oy += t.summa

            tolaganlar = []
            tolamaganlar = []
            tolaganlar_id = []
            for t in tolovlar:
                tolaganlar.append(Talaba.objects.get(id=t.talaba_ism.id))
                tolaganlar_id.append(t.talaba_ism.id)

            for talaba in talabalar:
                if talaba.id not in tolaganlar_id:
                    tolamaganlar.append(talaba)
            tolamaganlar_soni = len(tolamaganlar)
            guruhlar = Guruh.objects.all()
            leads = MalumotQoldirish.objects.all().count()
            promotorlar = Promotor.objects.all().count()
            kutayotganlar_soni = Kutayotganlar.objects.all().count()
            varonka = Voronka.objects.all()


            guruh_royxat = []
            for guruh in guruhlar:
                guruh_oquvchilari = guruh.azolik_set.all()
                guruh_tolovlari = guruh.tolov_set.all()
                yigildi = 0
                for oqituvchi in guruh.oqituvchi.oqituvchi_set.all():
                    oqituvchi = oqituvchi.ism + " " + oqituvchi.familya
                for tolov in guruh_tolovlari:
                    yigildi += tolov.summa

                g = {
                    'id':guruh.id,
                    'nomi':guruh.nomi,
                    'fan':guruh.fan.darsnomi,
                    'fan_rang':guruh.fan.rang,
                    'oqituvchi':oqituvchi,
                    'oquvchilar_soni':guruh_oquvchilari.count(),
                    'tolaganlar':guruh_tolovlari.count(),
                    'tolamaganlar':guruh_oquvchilari.count() - guruh_tolovlari.count(),
                    'umumiy_summ':guruh_oquvchilari.count() * guruh.narxi,
                    'yigildi':yigildi,
                }
                guruh_royxat.append(g)
            context = {
                'talabalar_1_foiz'  : talabalar_1_foiz,
                'guruhlar'          : guruhlar,
                'leads'             : leads,
                'promotorlar'       : promotorlar,
                'tolamaganlar_soni' : tolamaganlar_soni,
                'tolovlar'          : tolovlar,
                'pul_shu_oy'        : pul_shu_oy,
                'barchaOquvchi'     : barchaOquvchi,
                'fanlar'            : fanlar,
                'talabalar'         : talabalar,
                'kutayotganlar'     : kutayotganlar,
                'kutayotganlar_soni': kutayotganlar_soni,
                'tolaganlar'        : tolaganlar,
                'tolamaganlar'      : tolamaganlar[:15],
                'oqituvchilar'      : oqituvchilar,
                'guruh_royxat'      : guruh_royxat,
                'varonka'           : varonka,
                'active_dash'       : 'active'
            }
            return render(request, 'index_dash.html', context)

        else:
            return redirect('/login')
    else:
        return redirect('/login')


#################### Admin Email #############################################

def AdminMurojatlar(request):
    user = get_user(request)
    if user.is_authenticated:
        if user.is_staff:
            if request.method == 'POST':
                murojat_id = request.POST['murojat_id']
                murojat = MalumotQoldirish.objects.get(id=murojat_id)
                kut = Kutayotganlar.objects.create(ism_familya=murojat.ism, telefon=murojat.telefon,
                                            manzil=murojat.manzil)
                for fan in murojat.dars.all():
                    kut.dars.add(fan)
                murojat.delete();
            murojatlar = MalumotQoldirish.objects.all()
            kutayotganlar = Kutayotganlar.objects.all()
            print(murojatlar.count())
            # return render(request, 'apps_mailbox.html', {'murojatlar':murojatlar})
            context = {
                'murojatlar'    : murojatlar,
                'kutayotganlar' : kutayotganlar,
                'active_lead'   : 'active',
                'fanlar'        : Fan.objects.all()
            }
            return render(request, 'murojatlar.html', context)
        else:
            return redirect('/login')
    else:
        return redirect('/login')


#################### Kutayotganlar Form #############################################


def RoyxatgaOlishForm(request):
    user = get_user(request)
    if user.is_authenticated:
        if user.is_staff:

            if request.method == 'POST':

                ism = request.POST['ism']
                manzil = request.POST['manzil']
                tel = request.POST['telefon']
                fan = request.POST.getlist('fan')
                qayerdan_keldi = request.POST['qayerdan_keldi']
                bir_oila = request.POST.get('bir_oila')
                print(bir_oila)
                try:
                    taklif = request.POST['taklif']
                except:
                    taklif = None
                try:
                    pasport = request.FILES['pasport_rasm']
                except:
                    pasport = None
                kutayotgan = Kutayotganlar.objects.create(ism_familya=ism, telefon=tel, manzil=manzil, taklif_id=taklif,
                                            pasport=pasport, qayerdan_keldi=qayerdan_keldi, bir_oila_id=bir_oila)
                    
                        
                for f in fan:
                    fani = Fan.objects.get(id=f)
                    kutayotgan.dars.add(fani)
                messages.info(request, "Ism: {}".format(ism))
                messages.info(request, "Manzil: {}".format(manzil))
                messages.info(request, "Tel: {}".format(tel))
                for fan in kutayotgan.dars.all():
                    messages.info(request, "Fan: {}".format(fan.darsnomi))
                return redirect('/dashboard/kutayotganlar')



            fanlar = Fan.objects.all()
            talabalar = Talaba.objects.all()
            context = {
                'fanlar'                : fanlar,
                'talabalar'             : talabalar,
                'active_royxatga_olish' : 'active'
            }
            return render(request, 'royxatga_olish.html', context)
        else:
            return redirect('/login')
    else:
        return redirect('/login')


#################### Kutayotganlar To'liq Ro'yxat #############################################

def KutayotganlarToliq(request):
    user = get_user(request)
    if user.is_authenticated:
        if user.is_staff:
            if request.method == 'POST':
                ism = request.POST['ism']
                tel = request.POST['tel']
                manzil = request.POST['manzil']
                fan_id = request.POST.getlist('fan_id')
                guruh_id = request.POST['guruh']
                kutayotgan_id = request.POST['kutayotgan_id']
                qayerdan_keldi = request.POST['qayerdan_keldi']
                filyal = request.POST['filyal']
                bir_oila = request.POST.get('bir_oila')
                taklif_id = ''
                print(bir_oila, "bir oila")
                bonuslar = Bonus.objects.all()
                bonus_olganlar_id = []
                for bonus in bonuslar:
                    bonus_olganlar_id.append(bonus.talaba.id)

                if request.POST['taklif']:
                    taklif_id = request.POST['taklif']
                k = Kutayotganlar.objects.get(id=kutayotgan_id)
                g = Guruh.objects.get(id=guruh_id)

                if taklif_id:
                    taklif_qilgan = Talaba.objects.get(id=taklif_id)
                    talaba = Talaba(ism_familya=ism, telefon=tel, qayerdan_keldi=qayerdan_keldi, manzil=manzil, taklif_qilgan=taklif_id, filyal_id=filyal)
                    talaba.save()
                    Taklif.objects.create(taklif_qilgan=taklif_qilgan)
                    if Bonus.objects.filter(talaba_id=taklif_id).exists():
                        bonus = Bonus.objects.get(talaba_id=taklif_id)
                        bonus.takliflar_soni += 1
                        bonus.save()
                    else:
                        Bonus.objects.create(talaba_id=taklif_id, takliflar_soni=1)

                    for fan in fan_id:
                        fani = Fan.objects.get(id=fan)
                        print(fani)
                        talaba.fanlar.add(fani)
                        talaba.save()
                else:
                    talaba = Talaba(ism_familya=ism, qayerdan_keldi=qayerdan_keldi,telefon=tel, manzil=manzil, filyal_id=filyal)
                    talaba.save()
                    for fan in fan_id:
                        fani = Fan.objects.get(id=fan)
                        print(fani)
                        talaba.fanlar.add(fani)
                        talaba.save()
                if bir_oila:
                    bonus = Bonus.objects.create(talaba_id=talaba.id)
                    bonus.bir_oila.add(Talaba.objects.get(id=bir_oila).id)
                    bonus.save()
                    if bir_oila in bonus_olganlar_id:
                        bonus = Bonus.objects.get(talaba_id=bir_oila)
                        bonus.bir_oila.add(talaba.id)
                        bonus.save()
                    else:
                        bonus = Bonus.objects.create(talaba_id=bir_oila)
                        bonus.bir_oila.add(talaba.id)
                        bonus.save()

                messages.info(request, "{} O'quvchilarga qo'shildi".format(ism))
                Azolik.objects.create(talaba=talaba, guruh=g)
                k.delete()
            guruhlar = Guruh.objects.all()
            kutayotganlar = Kutayotganlar.objects.all()
            talabalar = Talaba.objects.all()
            Kutayotganlar.objects.filter(sana__lte=datetime.now() - timedelta(days=60)).delete()
            filyal = Filyal.objects.all()
            fanlar = Fan.objects.all()
            return render(request, 'kutayotganlar.html',
                        {'filyallar':filyal, 'kutayotganlar': kutayotganlar, 'guruhlar': guruhlar, 'fanlar': fanlar, 'talabalar':talabalar, 'kutayotganlar_active':'active'})
        else:
            return redirect('/login')
    else:
        return redirect('/login')

#################### Talabalar To'liq Ro'yxat #############################################

def TalabaToliqRoyxat(request):
    user = get_user(request)
    if user.is_authenticated:
        if user.is_staff:
            tolovlar = Tolov.objects.filter(oy_id=datetime.now().month)
            tolaganlar = []
            tolaganlar_id = []
            bonus = []
            chala_tolovqigan = []
            chala_tolovqigan_id = []
            talabalar = Azolik.objects.all()
            guruhlar = Guruh.objects.all()

            for t in tolovlar:
                if t.summa < t.guruh.narxi and t.summa > 0:
                    talaba = Talaba.objects.get(id=t.talaba_ism.id)
                    chala_tolovqigan.append(talaba)
                    chala_tolovqigan_id.append(talaba.id)
                    print (talaba, "talaba>>>>>>>>>>>>>>>")
                elif t.summa == 0:
                    bonus.append(t.talaba_ism.id)
                else:
                    talaba = Talaba.objects.get(id=t.talaba_ism.id)
                    tolaganlar.append(talaba)
                    tolaganlar_id.append(t.talaba_ism.id)
            context = {
                'bonus':bonus, 'guruhlar': guruhlar, 'tolaganlar': tolaganlar,
                'talabalar': talabalar, 'chala_tolovqigan':chala_tolovqigan,
                'chala_tolovqigan_id':chala_tolovqigan_id,
                'talabalar_active':"active"
            }
            return render(request, 'barcha_oquvchilar.html', context)
        else:
            return redirect('/login')
    else:
        return redirect('/login')


#################### O'qituvchi Qidiruv #############################################

def kutayotganlarga_qosh(request):
    if request.method == 'POST':
        murojat_id = request.POST['murojat_id']

        murojat = MalumotQoldirish.objects.get(id=murojat_id)
        Kutayotganlar.objects.create(ism_familya=murojat.ism, dars=murojat.dars, telefon=murojat.telefon,
                                     manzil=murojat.manzil)
        messages.add_message(request, messages.SUCCESS, "{} Kutayotganlarga qo'shildi".format(murojat.ism))
        murojat.delete()
        return redirect('/dashboard/admin-murojatlar')


#################### Test Natijalari kiritish Form #############################################

def TestNatijaForm(request):
    user = get_user(request)
    if user.is_authenticated:
        if request.method == 'POST':
            gr_id = request.POST['guruh_id']
            t_id = request.POST['talaba_id']
            natijasi = request.POST['test_natijasi']
            t = Talaba.objects.get(id=t_id)
            g = Guruh.objects.get(id=gr_id)

            TestNatijalari.objects.create(oquvchi=t, guruhi=g, natijasi=natijasi)
            messages.info(request, "Guruh: {}".format(g))
            messages.info(request, "O'quvchi: {}".format(t))
            messages.info(request, "Natija: {}".format(natijasi))
        guruhlar = Guruh.objects.all()
        # talabalar = Talaba.objects.all()
        return render(request, 'test_natija_kiritish.html', {'guruhlar': guruhlar})
    else:
        return redirect('/login')


######################Guruh talabalari##############################################################

def guruh_talabalari(request):
    if request.method == "GET":
        grid = request.GET['i']
        g = Guruh.objects.get(id=grid)
        guruh_talabalari = g.azolik_set.all()
        tolovlar = Tolov.objects.filter(oy_id=datetime.now().month)
        data = []
        global tolov
        tolov = 0
        talabalar = Talaba.objects.all()
        for talaba in guruh_talabalari:
            taklif = '─'
            print(talaba.id, "talabani id si")
            for t in tolovlar:
                if talaba.talaba.id == t.talaba_ism.id:
                    tolov = 1
                    break
                else:
                    tolov = 0
            for talaba1 in talabalar:
                if talaba1.id == talaba.talaba.taklif_qilgan:
                    taklif = talaba1.ism_familya
            data.append({
                'id': talaba.talaba.id,
                "ism": talaba.talaba.ism_familya,
                'guruh': g.nomi,
                'guruh_id': g.id,
                'tolov': tolov,
                'tel': talaba.talaba.telefon,
                'manzil': talaba.talaba.manzil,
                'taklif': taklif,
                'taklif_qilganlari': talaba.talaba.taklif_set.all().count(),
                'qayerdan_keldi':talaba.talaba.qayerdan_keldi,
                'filyal':talaba.talaba.filyal.nomi
            })
            print(data)
        return JsonResponse({'data': data}, safe=False)
    else:
        print("hato")
    return render(request, 'test_natija_kiritish.html')


####################### bonus olganlar $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def BonusOlganlar(request):
    if request.method == 'POST':
        talaba_id = request.POST['talaba_id']
        
        oy = datetime.now().month
        talaba = Talaba.objects.get(id=talaba_id)
        guruh = talaba.guruh_set.all()
        miqdor = 0
        if guruh.count() > 1:
            i = 0
            
            for g in guruh:
                if i == 0:
                    bonus = Bonus.objects.get(talaba_id=talaba.id)
                    miqdor += bonus.takliflar_soni * 50000
                    if bonus.bir_oila.all():
                        miqdor += (g.narxi / 100) * 10
                    if bonus.kam_taminlangan:
                        miqdor += (g.narxi / 100) * 10
                    miqdor += (g.narxi / 100) * 10
                    Tolov.objects.create(talaba_ism_id=talaba_id, guruh=g, summa=miqdor, oy_id=oy)
                    i += 1
                    bonus.takliflar_soni=0
                    bonus.save()
                else:
                    Tolov.objects.create(talaba_ism_id=talaba_id, guruh=g, summa=(g.narxi / 100) * 10, oy_id=oy)
        else:
            for g in guruh:
                bonus = Bonus.objects.get(talaba_id=talaba.id)
                miqdor += bonus.takliflar_soni * 50000
                if bonus.bir_oila.all():
                    miqdor += (g.narxi / 100) * 10
                if bonus.kam_taminlangan:
                    miqdor += (g.narxi / 100) * 10
                bonus.takliflar_soni=0
                bonus.save()
                
                Tolov.objects.create(talaba_ism_id=talaba_id, guruh=g, summa=miqdor, oy_id=oy)

                    
         
        # try:
        #     p = Promotor.objects.get(talaba_id=talaba_id)
        #     p.qancha_chaqirgan += 3
        # except:
        #     Promotor.objects.create(talaba_id=talaba_id, qancha_chaqirgan=3)

        bonus_olganlar = Taklif.objects.filter(taklif_qilgan=talaba).order_by('id')[:3]
        messages.info(request, " Tasdiqlandi")
        for b in bonus_olganlar:
            print(b)
            b.delete()
 

    talabalar = Talaba.objects.all()
    oylar = Oy.objects.all()
    bonuslar = Bonus.objects.all()
    bonus_olganlar_id = []
    for bonus in bonuslar:
        bonus_olganlar_id.append(bonus.talaba.id)
    for talaba in talabalar:
        if talaba.guruh_set.all().count() > 1:
            for bonus in bonuslar:
                if talaba.id in bonus_olganlar_id:
                    bonus.kop_fan = True
                    break
                else:
                    bonus = Bonus.objects.create(talaba_id=talaba.id, kop_fan=True)
                    break
            
    return render(request, 'bonuslar.html', {'bonuslar':bonuslar, 'talabalar': talabalar, "oylar": oylar, 'bonus_olgan_active':'active'})


######################Tolovlar#################################################
def TolovKiritish(request):
    user = get_user(request)
    if user.is_authenticated:
        i = 0
        if request.method == 'POST':
            gr_id = request.POST['gur_id']
            
            t_id = request.POST['tal_id']
            oy_id = request.POST['oy']
            summa = request.POST['pul']
            g = Guruh.objects.get(id=gr_id)
            t = Talaba.objects.get(id=t_id)
            print(t_id, oy_id)
            tol = Tolov.objects.filter(talaba_ism_id=t_id, oy_id=oy_id)
            print(len(tol), tol.count())
            if tol.count() == 1:
                # print(tol.oy.id, oy_id, "lkjlkjfdsfdskfjdlkfjlksdfj>>>>>>>>>>>>>>>>>>>")
                tol = tol.first()
                tol.summa += int(summa)
                tol.save()
            else:
                Tolov.objects.create(talaba_ism_id=t_id, guruh_id=gr_id, summa=summa, oy_id=oy_id)

            messages.info(request, "Guruh: {}".format(g))
            messages.info(request, "O'quvchi: {}".format(t.ism_familya))
            messages.info(request, "Miqdori: {}".format(summa))
            i = 1
        talabalar = Talaba.objects.all()
        hozirgi_oy = datetime.today().month
        tolovlar = Tolov.objects.filter(oy_id=hozirgi_oy)
        tolaganlar = []
        chala_tolovqigan = []
        chala_tolovqigan_id = []
        tolamaganlar = []
        tolaganlar_id = []
        
        for t in tolovlar:
            if t.summa >= t.guruh.narxi or t.summa >= t.talaba_ism.davomat_set.filter(keldi=1).count() * (t.guruh.narxi / 12):
                talaba = Talaba.objects.get(id=t.talaba_ism.id)
                tolaganlar.append(talaba)
                tolaganlar_id.append(t.talaba_ism.id)
            else:
                talaba = Talaba.objects.get(id=t.talaba_ism.id)
                chala_tolovqigan_id.append(talaba.id)
                tal = {
                    'id': t.talaba_ism.id,
                    'ism_familya':t.talaba_ism.ism_familya,
                    'guruh': t.guruh.nomi,
                    'guruh_id':t.guruh.id,
                    'telefon': t.talaba_ism.telefon,
                    'tolashi': t.talaba_ism.davomat_set.filter(keldi=1).count() * (t.guruh.narxi // 12),
                    'tolagan': t.summa,
                    }
                chala_tolovqigan.append(tal)
        for azo in Azolik.objects.all():
            if azo.talaba.id not in tolaganlar_id and azo.talaba.id not in chala_tolovqigan_id:
                tal = {
                    'id': azo.talaba.id,
                    'ism_familya':azo.talaba.ism_familya,
                    'guruh':  azo.guruh.nomi,
                    'guruh_id':azo.guruh.id,
                    'telefon': azo.talaba.telefon,
                    'tolashi': azo.talaba.davomat_set.filter(keldi=1).count() * (azo.guruh.narxi // 12),
                    'tolagan': azo.talaba.tolov_set.filter(talaba_ism_id=azo.talaba.id),
                    }
                tolamaganlar.append(tal)
        guruhlar = Guruh.objects.all()
        oylar = Oy.objects.all()



        print(i, "iiiiiiiiiiiiiii")
        return render(request, 'tolov_qilish.html',
                      {'i': i, 'tolomaganlar': tolamaganlar, 'talabalar': talabalar, 'tolovlar': tolovlar,
                       'guruhlar': guruhlar, 'oylar': oylar, 'chala_tolovqigan':chala_tolovqigan, 'tolov_active':"active"})
    else:
        return redirect('/login')


#################### Tolovlar #############################################

def TolovlarView(request):
    user = get_user(request)
    if user.is_authenticated:
        tolovlar = Tolov.objects.all()
        guruhlar = Guruh.objects.all()
        pul = 0
        for tolov in tolovlar:
            pul += tolov.summa
        print(pul)
        return render(request, 'barcha_tolovlar.html', {'pul': pul, 'tolovlar': tolovlar, 'guruhlar': guruhlar, 'tolovlar_active': 'active'})
    else:
        return redirect('/login')


#################### O'qituvchi davomat #############################################

def OqituvchiDavomat(request):
    user = get_user(request)
    if user.is_authenticated:
        guruhlari = user.guruh_set.all()
        return render(request, 'oqituvchi_davomat.html', {'guruhlari': guruhlari, 'oqituvchidavomat_active': 'active'})
    else:
        return redirect('/login')


#################### tolovdagi gr talabalar #############################################

def tolov_form_grtalabalar(request):
    if request.method == "GET":
        grid = request.GET['gr_id']
        g = Guruh.objects.get(id=grid)
        guruh_talabalari = g.azolik_set.all()
        data = []
        for talaba in guruh_talabalari:
            print(talaba.id, "tallaba id")
            data.append({
                't_id': talaba.talaba.id,
                "ism": talaba.talaba.ism_familya
            })

        return JsonResponse({'data': data}, safe=False)
    else:
        print("hato")
    return render(request, 'tolov_kiritish.html')


#################### Talabalar Dateil View #############################################
def OqituvchiQoshish(request):
    user = get_user(request)
    if user.is_authenticated:
        if request.method == 'POST':
            ism = request.POST['ism']
            familya = request.POST['familya']
            fan = request.POST.getlist('fan')
            tel = request.POST['telefon']
            manzil = request.POST['manzil']
            rasm = request.FILES['rasm']
            i = User.objects.latest('id')
            u_n = ism + str(i.id + 1)
            p = ism + familya[0] + str(i.id + 1)
            user = User.objects.create_user(username=u_n, password=p)
            user.save();
            o = Oqituvchi.objects.create(useri=user, ism=ism, familya=familya, manzil=manzil, tel=tel, rasm=rasm)
            for f in fan:
                fani = Fan.objects.get(id=f)
                o.fani.add(fani)
            messages.add_message(request, messages.SUCCESS, "Username: {}".format(u_n))
            messages.add_message(request, messages.SUCCESS, 'Parol: {}'.format(p))
            return redirect('oqituvchi-qoshish')
        fanlar = Fan.objects.all()
        oqituvchilar = Oqituvchi.objects.all()
        return render(request, 'oqtuvchi_qoshish.html', {'fanlar': fanlar, 'oqituvchilar': oqituvchilar, 'oqituvchiqosh_active': 'active'})
    else:
        return redirect('/login')


#################### Guruhlar #############################################

def Guruhlar(request):
    user = get_user(request)
    if user.is_authenticated:
        if request.method == "POST":
            gr_nomi = request.POST['gr_nomi']
            fan = request.POST['fan']
            narx = request.POST['narx']
            oqituvchi = request.POST['oqituvchi']
            hafta_kunlari = request.POST.getlist('kun')
            soat = request.POST['soat']

            guruh = Guruh.objects.create(nomi=gr_nomi, fan_id=fan, oqituvchi_id=oqituvchi, narxi=narx, soat=soat)
            for kun in hafta_kunlari:
                guruh.kunlari.add(kun)
            messages.info(request, 'Guruh nomi:{}'.format(gr_nomi))
            messages.info(request, "Fan: {}".format(Fan.objects.get(id=fan)))
            return redirect('/dashboard/guruhlar')
        guruhlar = Guruh.objects.all()
        fanlar = Fan.objects.all()
        talabalar = Talaba.objects.all()
        oqituvchilar = Oqituvchi.objects.all()
        hafta_kunlari = HaftaKunlari.objects.all()
        context = {
            'talabalar':talabalar, 'guruhlar': guruhlar, 
            'fanlar': fanlar, 'oqituvchilar': oqituvchilar, 
            'guruhlar_active': 'active', 'hafta_kunlari': hafta_kunlari
        }
        return render(request, 'guruhlar.html', context)
    else:
        return redirect('/login')

def guruhga_qosh(request):
    if request.method == 'POST':
        gr_id = request.POST['gr_id']
        talaba_id = request.POST.getlist['talaba']
        for talaba_id in talaba_idlar:
            azo = Azolik.objects.create(talaba_id=talaba_id, guruh_id=gr_id)
            azo.save()
            messages.info(request, "Talaba: {}".format(azo.talaba.ism_familya))
        messages.info(request, 'Guruh nomi:{}'.format(gr_nomi))

#################### Guruhga talaba qo'shish ############################################

def grga_talaba_qosh(request):
    user = get_user(request)
    if user.is_authenticated:
        if request.method == 'POST':
            talaba_idlar = request.POST['oquvchi']
            gr_id = request.POST['guruh_id']
            for talaba_id in talaba_idlar:
                azo = Azolik.objects.create(talaba_id=talaba_id, guruh_id=gr_id)
                azo.save()
                messages.info(request, "Talaba: {}".format(azo.talaba.ism_familya))
        messages.info(request, 'Guruh nomi:{}'.format(Guruh.objects.get(id=gr_id)))
        return redirect('/dashboard/guruhlar/')
    else:
        return redirect('/login')


#################### O'qituvchi dash ############################################

def OqituvchiDash(request):
    user = get_user(request)

    if user.is_authenticated:
        print('user oqituvchi', user.oqituvchi_set.all())
        if not user.is_superuser:
            oquvchilar = 0
            pul = 0
            talabalar = []
            tolaganlar = []
            tolamaganlar = []
            tolaganlar_id = []
            tolamaganlar_id = []
            tolovlar_id = []
            tolamaganlar_soni = 0
            guruhlari = user.guruh_set.all()

            for g in guruhlari:
                oquvchilar += g.azolik_set.all().count()
                for tol in Tolov.objects.filter(guruh_id=g.id):
                    tolovlar_id.append(tol.talaba_ism.id)
                    pul += tol.summa
                for t in g.azolik_set.all():
                    talabalar.append(t)
                print(talabalar)
                if tolovlar_id:
                    for t in g.azolik_set.all():
                        if t.talaba.id in tolovlar_id:
                            tolaganlar.append(t)
                            tolaganlar_id.append(t.talaba.id)
                        else:
                            tolamaganlar.append(t)
                            tolamaganlar_id.append(t.talaba.id)

                        tolamaganlar_soni = len(tolamaganlar)
                else:
                    tolamaganlar_soni = len(talabalar)

            print(tolamaganlar_soni)
            context = {
                'guruhlari': guruhlari, 'tolaganlar': tolaganlar, 'oqituvchi_active':'active',
                'pul': pul, 'oquvchilar': oquvchilar, 'talabalar': talabalar,
                'tolamaganlar_id': tolamaganlar_id, 'tolaganlar_id': tolaganlar_id,
                'tolamaganlar': tolamaganlar, 'tolamaganlar_soni': tolamaganlar_soni,
            }
            return render(request, 'oqituvchi_dashboard.html', context)
        else:
            return redirect('/login')
    else:
        return redirect('/login')


#################### Talabalar Dateil View ############################################

def fan_oqituvchilari(request):
    if request.method == "GET":
        fan_id = request.GET['fan_id']
        fan = Fan.objects.get(id=fan_id)
        fan_oqituvchilar = fan.oqituvchi_set.all()
        data = []
        if fan_oqituvchilar:
            for oqituvchi in fan_oqituvchilar:
                print(oqituvchi.id, "oqituvchi id")
                data.append({
                    'id': oqituvchi.useri.id,
                    'ism': oqituvchi.ism,
                    'fam': oqituvchi.familya
                })
        else:
            print('hato bor')

        return JsonResponse({'data': data}, safe=False)
    else:
        print("hato")
    return render(request, 'guruhlar.html')


####################### o'qituvchi o'chirish ###################################

def oqituvchi_ochirish(request):
    if request.method == "POST":
        o_id = request.POST['oqituvchi_id']
        o = Oqituvchi.objects.get(id=o_id)
        u = User.objects.get(id=o.useri.id)
        print("oqituvhci:", o, "useri:", u)
        messages.add_message(request, messages.INFO, "{} {}".format(o.ism, o.familya))
        o.delete()
        u.delete()

        return redirect('/dashboard/oqituvchi-qoshish/')
    return redirect('/')


#################### Talabalar Dateil View #############################################

class TalabalarDateilView(DetailView):
    model = Talaba
    template_name = 'talaba.html'
    context_object_name = 'talaba'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['talabalar'] = Talaba.objects.all()

        return context


class GuruhTolaganlarDetail(DetailView):
    model = Guruh
    template_name = 'barcha_tolovlar.html'
    context_object_name = 'guruh_tolagan'


#################### Guruh Dateil View #############################################

class GuruhDetailView(DetailView):
    model = Guruh
    template_name = 'guruh.html'
    context_object_name = 'guruh'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['oquvchilar'] = Talaba.objects.all()
        context['tolaganlar'] = Tolov.objects.filter(sana__year=datetime.now().year, sana__month=datetime.now().month)
        return context

def guruh(request):
    if request.method == 'GET':
        guruh_id = request.GET['guruh_id']
        guruh = Guruh.objects.get(id=guruh_id)
        tolaganlar_id = []
        for tolagan in guruh.tolov_set.all():
            tolaganlar_id.append(tolagan.id)
        tolamaganlar = []
        for talaba in guruh.azolik_set.all():
            if talaba.id not in tolaganlar_id:
                tolamaganlar.append(talaba)

        chalalar = Tolov.objects.filter(guruh_id=guruh_id, summa__lt = guruh.narxi)
        return render(request, 'guruh.html',{'chalalar':chalalar, 'guruh':guruh, 'tolamaganlar':tolamaganlar})
        
        

def GuruhDView(request):
    guruh = ''
    user = get_user(request)
    if request.method == 'POST':
       gur_id = request.POST['guruh_id']
       print(guruh, gur_id)
       guruh = Guruh.objects.get(id=gur_id)
       print(guruh.azolik_set.all())
       data = []
       print(guruh.id)
       for talaba in guruh.azolik_set.all():
           t ={
               'id' : talaba.talaba.id,
               'ism_familya': talaba.talaba.ism_familya,
               'guruh' : talaba.guruh.nomi,
               'telefon' : talaba.talaba.telefon,
               'qoldirgan' : talaba.talaba.davomat_set.filter(keldi=0, sana__month=datetime.now().month, sana__year=datetime.now().year).count(),

           }
           data.append(t)



    return render(request, 'davomat_royhat.html', {'guruh_t':data, 'guruh':guruh, 'guruhlari':user.guruh_set.all(), 'davomat_active':'active'})

#################### Murojat Dateil View #############################################

class MutojatlarDateilView(DetailView):
    model = MalumotQoldirish
    template_name = 'admin-emails.html'
    context_object_name = 'murojat1'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['murojatlar'] = MalumotQoldirish.objects.all()
        return context


#######################<< Davomat >>#########################

def PromotorView(request):
    promotorlar = Promotor.objects.all()
    return render(request, 'promotorlar.html', {'promotorlar': promotorlar, 'promotor_active':'active'})

def DavomatView(request):
    user = get_user(request)

    if user.is_authenticated:
        if user.is_staff:
            return redirect('/dashboard')
        else:
            if request.method == 'POST':
                try:
                    print("try inchida")
                    bor_yoq = request.POST.getlist('bor-yoq')
                    print(bor_yoq, "try")
                except:
                    print("exept ichida")
                    bor_yoq = [0]
                g = request.POST['gur_id']
                print(bor_yoq, "bor yo'q")
                guruh = Guruh.objects.get(id=g)
                gr_talabalar = guruh.azolik_set.all()
                print(gr_talabalar)
                for t in gr_talabalar:
                    print(bor_yoq, "forni icida")

                    if str(t.talaba.id) in bor_yoq:
                        Davomat.objects.create(oqituvchi=user, talaba_id=t.talaba.id, guruh=guruh, keldi=1)
                    else:
                        Davomat.objects.create(oqituvchi=user, talaba_id=t.talaba.id, guruh=guruh, keldi=0)
                return redirect('/dashboard/davomat')
    davomat_royxat = user.davomat_set.all()
    guruhlari = user.guruh_set.all()
    return render(request, 'davomat_royhat.html', {'davomat_royxat': davomat_royxat, 'guruhlari':guruhlari})


def xato404(request, exception):
    return render(request, '404.html')


def FanQosh(request):
    if request.method == 'POST':
        fan_nomi = request.POST['fan']
        rang = request.POST['rang']
        Fan.objects.create(darsnomi=fan_nomi, rang=rang)
        return redirect('/dashboard')
    return redirect('/dashboard')


def HisobotView(request):
    if request.method == 'POST':
        hisobot = request.POST['hisobot']
        Hisobot.objects.create(hisobot=hisobot)
        messages.info(request, "Hisobot Yuborildi")
    hisobotlar = Hisobot.objects.all()

    return render(request, 'hisobot.html', {'hisobotlar': hisobotlar, 'hisobot_active':'active'})





def FanOchirish(request):
    if request.method == 'POST':
        fan_id = request.POST['fan_ochir']
        fan = Fan.objects.get(id=fan_id)
        fan.status = 0
        fan.save()

        print('fan ochirirldi')
    print('pstmans')
    return redirect('/dashboard')

def hisobot_saralash(request):
    if request.method == 'GET':
        dan = request.GET['dan']
        gacha = request.GET['gacha']
        data = []
        hisobot_sarasi = Hisobot.objects.filter(sana__gte=dan, sana__lt=gacha)
        for hisobot in hisobot_sarasi:
            data.append({
                    'id':hisobot.id,
                    'hisobot':hisobot.hisobot,
                    'sana':hisobot.sana
                })
        return JsonResponse({'data': data}, safe=False)
    return render(request, 'hisobot.html')


def leads(request):
    if request.method == 'POST':
        try:
            murojat_id = request.POST['murojat_id']
            malumot = request.POST['malumot']
            mq = MalumotQoldirish.objects.get(id=murojat_id)
            mq.toliq = malumot
            mq.save()
            return redirect('/dashboard/admin-murojatlar/')
        except:
            ism = request.POST['ism']
            tel = request.POST['telefon']
            toliq = request.POST['malumot']
            dars = request.POST.getlist('fan')
            manzil = request.POST['manzil']
            qayerdan_keldi = request.POST['qayerdan_keldi']

            lead = MalumotQoldirish.objects.create(ism=ism, telefon=tel, toliq=toliq, manzil=manzil, qayerdan_keldi=qayerdan_keldi)
            for fan in dars:
                fan = Fan.objects.get(id=fan)
                lead.dars.add(fan)
            return redirect('/dashboard/admin-murojatlar/')
        return redirect('/dashboard/admin-murojatlar/')


def lead_toifa(request):
    if request.method == 'POST':
        lead_id = request.POST['murojat_id']
        toifa = request.POST['toifa']

        lead = MalumotQoldirish.objects.get(id=lead_id)
        lead.toifa = toifa
        lead.save()
        return redirect('/dashboard/admin-murojatlar/')
    return redirect('/dashboard/admin-murojatlar/')


def talaba_sharoit_qosh(request):
    if request.method == 'POST':
        sharoit = request.POST['sharoit']
        talaba_id = request.POST['talaba_id']

        talaba = Talaba.objects.get(id=talaba_id)
        talaba.sharoit = sharoit
        talaba.save()
        bor = False
        if sharoit == "Kam taminlangan":
            for b in Bonus.objects.all():
                if talaba.id == b.talaba.id:
                    bor = True
                    break
            
            if bor:
                bonus = Bonus.objects.get(talaba_id=talaba.id)
                bonus.kam_taminlangan = True
                bonus.save()
            else:
                bonus = Bonus.objects.create(talaba_id=talaba_id, kam_taminlangan=True)
            return redirect("/dashboard/talaba/{}/".format(talaba_id))
        else:
            for b in Bonus.objects.all():
                if talaba.id == b.talaba.id:
                    bor = False
                    break
            return redirect("/dashboard/talaba/{}/".format(talaba_id))
    return redirect("/dashboard/talaba/{}/".format(talaba_id))


def  Kitob_olganlar(request):
    if request.method == 'POST':
        uslub = request.POST.get('uslub')
        if uslub == 'topshirish':
            holat = request.POST['holat']
            kitob_olgan_id = request.POST['kitob_olgan_id']
            kitob_olgan = KitobOlganlar.objects.get(id=kitob_olgan_id)
            kitob_olgan.holat = holat
            kitob_olgan.save()
            
            return redirect('/dashboard/kitob-olganlar/')

        talaba_id = request.POST['talaba_id']
        kitob = request.POST['kitob']
        qaytaradi = request.POST['qaytaradi']

        kitob_olgan = KitobOlganlar.objects.create(talaba_id=talaba_id, kitob=kitob, qaytaradi=qaytaradi)

        return redirect('/dashboard/kitob-olganlar/')
    
    guruhlar = Guruh.objects.all()
    kitob_olganlar = KitobOlganlar.objects.filter(holat=1)

    return render(request, 'kitob-olganlar.html', {'kitob_olganlar':kitob_olganlar, 'guruhlar':guruhlar})