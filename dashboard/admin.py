from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group, User

# Register your models here.
admin.site.register(Filyal)
admin.site.site_header = "Compass Admin Panel"
admin.site.site_title = "Compass API"
admin.site.index_title = "Compass"

admin.site.register(Fan)
admin.site.register(HaftaKunlari)
admin.site.register(Voronka)
admin.site.register(Bonus)

@admin.register(Hisobot)
class HisobotModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'hisobot', 'sana')
    list_display_links = ('id', 'hisobot')

@admin.register(Taklif)
class TaklifAdmin(admin.ModelAdmin):
    list_display = ('id', 'taklif_qilgan')
    list_display_links = ('id', 'taklif_qilgan')


@admin.register(Talaba)
class TalabaAdmin(admin.ModelAdmin):
    list_display = (
    'id', "ism_familya", "telefon", "manzil", 'taklif_qilgan', 'bonus', 'bonus_ishlatilganlari', 'sana')
    list_display_links = ('id', 'ism_familya')
    list_filter = ('manzil',)
    search_fields = ('id', "ism_familya")


@admin.register(Guruh)
class GuruhAdmin(admin.ModelAdmin):
    list_display = ('id', "nomi", "fan", "oqituvchi", 'narxi')
    list_display_links = ('id', "nomi", "fan", "oqituvchi", 'narxi')


@admin.register(Oqituvchi)
class OqituvchiAdmin(admin.ModelAdmin):
    list_display = ("useri", "ism", "familya", "tel", 'rasm')


@admin.register(Azolik)
class AzolikAdmin(admin.ModelAdmin):
    list_display = ("id", "talaba", "guruh", "qoshilgan_kun")


@admin.register(Tolov)
class TolovAdmin(admin.ModelAdmin):
    list_display = ("id", "guruh", "talaba_ism", 'oy', 'summa', 'sana')
    date_hierarchy = ('sana')


@admin.register(Kutayotganlar)
class KutayotganlarAdmin(admin.ModelAdmin):
    list_display = ("id", "ism_familya", 'manzil', 'telefon', 'taklif')


@admin.register(Davomat)
class DavomatAdmin(admin.ModelAdmin):
    list_display = ('id', 'sana', 'talaba', 'guruh', 'keldi')

@admin.register(KitobOlganlar)
class KitobOlganlarAdmin(admin.ModelAdmin):
    list_display = ('id', 'talaba', 'kitob', 'olgan_sana', 'qaytaradi')
    list_display_links = ('id', 'talaba', 'kitob', 'olgan_sana', 'qaytaradi')

@admin.register(Promotor)
class PromotorAdmin(admin.ModelAdmin):
    list_display = ('id', 'talaba')

admin.site.register(Oy)
admin.site.register(TestNatijalari)
admin.site.unregister(Group)
# admin.site.unregister(User)
admin.site.register(Kitob)