from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(MalumotQoldirish)
admin.site.register(Galareya)
admin.site.register(malumot)
admin.site.register(Slider)
admin.site.register(Events)
admin.site.register(Haqimizda)
admin.site.register(Tarmoq)
admin.site.register(Contact)
admin.site.register(Bolim_izox)
@admin.register(Bitirganlar)
class BitirganlarAdmin(admin.ModelAdmin):
    list_display = ('id','muvofaqqiyatli', 'sertifikat_olganlar')
    list_display_links = ('muvofaqqiyatli', 'sertifikat_olganlar')
