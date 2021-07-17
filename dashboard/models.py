from django.db import models
from django.contrib.auth.models import User


# Create your models here.


######################< FAN >##############################

class Fan(models.Model):
    darsnomi = models.CharField(max_length=100)
    rang = models.CharField(max_length=10)
    status = models.IntegerField(default=1)

    def __str__(self):
        return self.darsnomi

    class Meta:
        verbose_name_plural = 'Fanlar'


#########################<< O'QITUVCHI >>###########################

class Oqituvchi(models.Model):
    useri = models.ForeignKey(User, on_delete=models.CASCADE)
    ism = models.CharField(max_length=100)
    familya = models.CharField(max_length=100)
    tel = models.CharField(max_length=17)
    fani = models.ManyToManyField(Fan, null=True, blank=True)
    rasm = models.ImageField(upload_to='teacher_potho')
    manzil = models.CharField(max_length=100, null=True, blank=True)
    class Meta:
        verbose_name_plural = "O'qituvchilar"

    def __str__(self):
        return self.ism + "  " + self.familya


##########################<< TALABA >>##########################

class Filyal(models.Model):
    nomi = models.CharField(max_length=100)
    manzil = models.CharField(max_length=50)
    sana = models.DateField(auto_now_add=True)

class Talaba(models.Model):

    ism_familya = models.CharField(max_length=200)
    telefon = models.CharField(max_length=17)
    manzil = models.CharField(max_length=300)
    taklif_qilgan = models.IntegerField(null=True, blank=True)
    qayerdan_keldi = models.CharField(max_length=50, default='─')
    fanlar = models.ManyToManyField(Fan, null=True, blank=True)
    bonus = models.IntegerField(default=0)
    bonus_ishlatilganlari = models.IntegerField(default=0)
    filyal = models.ForeignKey(Filyal, on_delete=models.CASCADE)
    sana = models.DateField(auto_now_add=True)
    sharoit = models.CharField(max_length=50, null=True, blank=True)
    bir_oila = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Talabalar'

    def __str__(self):
        return self.ism_familya


######################### takliflar ###############################

class Taklif(models.Model):
    taklif_qilgan = models.ForeignKey(Talaba, on_delete=models.SET_NULL, null=True, blank=True)
    # taklif_qilingan = models.ForeignKey(Talaba, on_delete=models.SET_NULL, null=True, blank=True)


########################<< KUTAYOTGANLAR >>########################

class Kutayotganlar(models.Model):
    ism_familya = models.CharField(max_length=200)
    dars = models.ManyToManyField(Fan, null=True, blank=True)
    telefon = models.CharField(max_length=17)
    manzil = models.CharField(max_length=300)
    taklif = models.ForeignKey(Talaba, on_delete=models.CASCADE, null=True, blank=True)
    qayerdan_keldi = models.CharField(max_length=50)
    pasport = models.ImageField(upload_to='pasport', blank=True, null=True)
    sana = models.DateField(auto_now_add=True)
    bir_oila = models.ForeignKey(Talaba, on_delete=models.SET_NULL, null=True, blank=True, related_name='oila')

    class Meta:
        verbose_name_plural = "Kutayotganlar"

    def __str__(self):
        return self.ism_familya + " || " + self.telefon


###########################<< GURUH >>###########################

class HaftaKunlari(models.Model):
    nomi = models.CharField(max_length=20)

    def __str__(self):
        return self.nomi

class Guruh(models.Model):
    nomi = models.CharField(max_length=100)
    fan = models.ForeignKey(Fan, on_delete=models.CASCADE)
    oqituvchi = models.ForeignKey(User, on_delete=models.CASCADE)
    oquvchi = models.ManyToManyField(Talaba, through='Azolik')
    narxi = models.IntegerField()
    kunlari = models.ManyToManyField(HaftaKunlari)
    soat = models.CharField(max_length=10)



    class Meta:
        verbose_name_plural = 'Guruhlar'

    def __str__(self):
        return str(self.nomi)


#########################<< Azolik >>#############################

class Azolik(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    guruh = models.ForeignKey(Guruh, on_delete=models.CASCADE)
    qoshilgan_kun = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Azolik"


########################<< OY >>####################################

class Oy(models.Model):
    oy_nomi = models.CharField(max_length=50)

    def __str__(self):
        return self.oy_nomi

    class Meta:
        verbose_name_plural = "Oylar"





########################<< TO'LOV >> ###############################


class Tolov(models.Model):
    guruh = models.ForeignKey(Guruh, on_delete=models.CASCADE)
    talaba_ism = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    oy = models.ForeignKey(Oy, on_delete=models.CASCADE)
    summa = models.IntegerField(default=0)
    sana = models.DateField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Tolovlar"

    def __str__(self):
        return self.talaba_ism.ism_familya + " | " + self.guruh.nomi


#######################<< Test natijalari >>#########################

class TestNatijalari(models.Model):
    oquvchi = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    guruhi = models.ForeignKey(Guruh, on_delete=models.CASCADE)
    natijasi = models.IntegerField()

    def __str__(self):
        return self.oquvchi.ism_familya


#######################<< Davomat >>#########################

class Davomat(models.Model):
    oqituvchi = models.ForeignKey(User, on_delete=models.CASCADE)
    sana = models.DateField(auto_now_add=True)
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    guruh = models.ForeignKey(Guruh, on_delete=models.CASCADE)
    keldi = models.IntegerField()


class Promotor(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    


class Hisobot(models.Model):
    hisobot = models.TextField()
    sana = models.DateField(auto_now_add=True)


class Voronka(models.Model):
    rasm1 = models.ImageField(upload_to='varonka')
    rasm2 = models.ImageField(upload_to='varonka')
    rasm3 = models.ImageField(upload_to='varonka')
    rasm4 = models.ImageField(upload_to='varonka')


# Barcha bo'nus olishi kerak bo'lganlar uchun

class Bonus(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE, related_name="oquvchi")
    takliflar_soni = models.IntegerField(default=0)
    bir_oila = models.ManyToManyField(Talaba, related_name='birOila', null=True, blank=True)
    kam_taminlangan = models.BooleanField(default=False)
    kop_fan = models.BooleanField(default=False)
    sana = models.DateField(auto_now_add=True)
    

class Kitob(models.Model):
    nomi = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nomi


class KitobOlganlar(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    kitob = models.CharField(max_length=50)
    olgan_sana = models.DateField(auto_now_add=True)
    qaytaradi = models.DateField()
    holat = models.IntegerField(choices=((1, "Topshirmagan"), (2, "Topshirgan")), default=1)

    def __str__(self) -> str:
        return self.talaba.ism_familya
