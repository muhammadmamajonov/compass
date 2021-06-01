from django.db import models
from dashboard.models import Fan


class MalumotQoldirish(models.Model):
    ism = models.CharField(max_length=50)
    telefon = models.CharField(max_length=17)
    toliq = models.TextField()
    manzil = models.CharField(max_length=300)
    qayerdan_keldi = models.CharField(max_length=50)
    toifa = models.CharField(max_length=50, default="Qayta aloqaga chiqmagan")
    dars = models.ManyToManyField(Fan, null=True, blank=True)
    sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ism + " || " + self.telefon

    class Meta:
        verbose_name_plural = "Murojatlar"


############################# Galareya ###############

class Galareya(models.Model):
    nomi = models.CharField(max_length=100)
    rasm = models.ImageField(upload_to="gallery")

    def __str__(self):
        return self.nomi


class Events(models.Model):
    nomi = models.CharField(max_length=100)
    rasm = models.ImageField(upload_to='events')
    izox = models.TextField()
    sana = models.DateField()

    def __str__(self):
        return self.nomi


class Slider(models.Model):
    rasm = models.ImageField(upload_to='slider_rasm')


class malumot(models.Model):
    nomi = models.CharField(max_length=50)
    toliq = models.TextField()
    rasm = models.ImageField(upload_to='malumotlar_rasm')

    class Meta:
        verbose_name = "O'quv markaz haqida ma'lumot"
        verbose_name_plural = "O'quv markaz haqida ma'lumotlar"
    def __str__(self):
        return self.nomi
        
class Haqimizda(models.Model):
    rasm = models.ImageField(upload_to='haqimizda')
    qisqa = models.CharField(max_length=100)
    toliq = models.TextField()

    def __str__(self):
        return self.qisqa

    class Meta:
        verbose_name = "Biz haqimizda"
        verbose_name_plural = "Biz haqimizda"
    

class Tarmoq(models.Model):
    tarmoq_nomi = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='tarmoq_icon', null=True, blank=True)
    url = models.URLField(verbose_name="Ijtimoiy tarmoqdagi sahifani usernamei")

    def __str__(self):
        return self.tarmoq_nomi
    
class Contact(models.Model):
    manzil = models.CharField(max_length=100)
    telefon = models.CharField(max_length=17)
    email = models.EmailField()


    def __str__(self):
        return self.manzil
    

class Bolim_izox(models.Model):
    galareya = models.CharField(max_length=100)
    oqituvchi = models.CharField(max_length=100)
    tadbirlar = models.CharField(max_length=100)
    murojaat = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Bo'limlarga izoxlar"
        verbose_name_plural = "Bo'limlarga izoxlar"

class Bitirganlar(models.Model):
    muvofaqqiyatli = models.PositiveIntegerField(verbose_name="Muvofaqqiyatli bitirganlar")
    sertifikat_olganlar = models.PositiveIntegerField(verbose_name="Sertifikat olganlar")

    def __str__(self):
        return "Bitirganlar va Sertifikat olganlar"

    class Meta:
        verbose_name = "Bitirganlar va Sertifikat olganla"
        verbose_name_plural = "Bitirganlar va Sertifikat olganla"
        
    