from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('', views.AdminDash, name='admin-dash'),
    path('gr-tolamaganlar/', views.guruh_tolamaganlar),
    path('gr-ga-talaba-qosh/', views.grga_talaba_qosh, name='gr-t-qosh'),
    path('guruh-talabalari/', views.guruh_talabalari),
    path('fan-oqituvchilari/', views.fan_oqituvchilari, name='fan_oqituvchilari'),
    path('guruhlar/', views.Guruhlar, name='guruhlar'),
    path('tolov_form_grtalabalar/', views.tolov_form_grtalabalar),
    path('test-natija-kiritish/', views.TestNatijaForm, name="test-natija-form"),
    path('talabalar/', views.TalabaToliqRoyxat, name='talabalar'),
    path('royhatga-olish/', views.RoyxatgaOlishForm, name='royxat-olish-form'),
    path('kutayotganlar/', views.KutayotganlarToliq, name='kutayotganlar' ),
    path('oqituvchi-qoshish/', views.OqituvchiQoshish, name='oqituvchi-qoshish'),
    path('tolov-kiritish/', views.TolovKiritish, name='tolov-kiritish'),
    path('tolovlar/', views.TolovlarView, name='tolovlar'),
    path('oqituvchi-dash/', views.OqituvchiDash, name='oqituvchi_dash'),
    path('oqituvchi-ochirish/', views.oqituvchi_ochirish, name='oqituvchi-ochirish'),
    path('admin-murojatlar/', views.AdminMurojatlar, name='admin-murojatlar'),
    path('kutayotganlarga_qosh/', views.kutayotganlarga_qosh, name='kutayotganlarga_qosh'),
    path('murojat-deteil/<int:pk>/', views.MutojatlarDateilView.as_view(), name='murojat-deteil'),
    path('talaba-deteil/<int:pk>/', views.TalabalarDateilView.as_view(), name='talaba-deteil'),
    path('guruh/<int:pk>/', views.GuruhDetailView.as_view(), name='guruh'),
    path('guruh-tolagan/<int:pk>/', views.GuruhTolaganlarDetail.as_view(), name='guruh-tolaganlar'),
    path('oqituvchi-davomat/', views.OqituvchiDavomat, name='oqituvchi-davomat'),
    path('bonus-olganlar/', views.BonusOlganlar, name='bonus-olganlar'),
    path('chart/', views.Chart, name = 'chart'),
    path('davomat/', views.DavomatView, name = 'davomat'),
    path('promotorlar/', views.PromotorView, name='promotorlar'),
    path('fan-qosh/', views.FanQosh, name='fan-qosh'),
    path('hisobot/', views.HisobotView, name='hisobot'),
    path('fan-ochir/', views.FanOchirish, name = 'fan-ochir'),
    path('hisobot_saralash/', views.hisobot_saralash, name = 'hisobot_saralash'),
    path('guruh-t/', views.GuruhDView, name = 'guruh-d'),
    path('leads/', views.leads, name = 'leads'),
    path('talaba/<int:pk>/', views.TalabalarDateilView.as_view(), name='talaba'),
    path('lead_toifa/', views.lead_toifa, name = 'lead_toifa'),
    path('guruh-tolamagan/', views.guruh, name = 'guruh-tolamagan'),
    path('talaba-sharoit-qosh/', views.talaba_sharoit_qosh, name = 'talaba_sharoit_qosh'),
    path('kitob-olganlar/', views.Kitob_olganlar, name='kitob_olganlar')

]
