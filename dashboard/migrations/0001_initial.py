# Generated by Django 3.1.4 on 2021-05-31 12:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Azolik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qoshilgan_kun', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Azolik',
            },
        ),
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('darsnomi', models.CharField(max_length=100)),
                ('rang', models.CharField(max_length=10)),
                ('status', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name_plural': 'Fanlar',
            },
        ),
        migrations.CreateModel(
            name='Filyal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100)),
                ('manzil', models.CharField(max_length=50)),
                ('sana', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Guruh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100)),
                ('narxi', models.IntegerField()),
                ('soat', models.CharField(max_length=10)),
                ('fan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.fan')),
            ],
            options={
                'verbose_name_plural': 'Guruhlar',
            },
        ),
        migrations.CreateModel(
            name='HaftaKunlari',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Hisobot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hisobot', models.TextField()),
                ('sana', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Oy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oy_nomi', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Oylar',
            },
        ),
        migrations.CreateModel(
            name='Talaba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism_familya', models.CharField(max_length=200)),
                ('telefon', models.CharField(max_length=17)),
                ('manzil', models.CharField(max_length=300)),
                ('taklif_qilgan', models.IntegerField(blank=True, null=True)),
                ('qayerdan_keldi', models.CharField(default='─', max_length=50)),
                ('bonus', models.IntegerField(default=0)),
                ('bonus_ishlatilganlari', models.IntegerField(default=0)),
                ('sana', models.DateField(auto_now_add=True)),
                ('sharoit', models.CharField(blank=True, max_length=50, null=True)),
                ('bir_oila', models.IntegerField(blank=True, null=True)),
                ('fanlar', models.ManyToManyField(blank=True, null=True, to='dashboard.Fan')),
                ('filyal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.filyal')),
            ],
            options={
                'verbose_name_plural': 'Talabalar',
            },
        ),
        migrations.CreateModel(
            name='Voronka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm1', models.ImageField(upload_to='varonka')),
                ('rasm2', models.ImageField(upload_to='varonka')),
                ('rasm3', models.ImageField(upload_to='varonka')),
                ('rasm4', models.ImageField(upload_to='varonka')),
            ],
        ),
        migrations.CreateModel(
            name='Tolov',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summa', models.IntegerField(default=0)),
                ('sana', models.DateField(auto_now_add=True, null=True)),
                ('guruh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.guruh')),
                ('oy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.oy')),
                ('talaba_ism', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.talaba')),
            ],
            options={
                'verbose_name_plural': 'Tolovlar',
            },
        ),
        migrations.CreateModel(
            name='TestNatijalari',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('natijasi', models.IntegerField()),
                ('guruhi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.guruh')),
                ('oquvchi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.talaba')),
            ],
        ),
        migrations.CreateModel(
            name='Taklif',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taklif_qilgan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.talaba')),
            ],
        ),
        migrations.CreateModel(
            name='Promotor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talaba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.talaba')),
            ],
        ),
        migrations.CreateModel(
            name='Oqituvchi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=100)),
                ('familya', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=17)),
                ('rasm', models.ImageField(upload_to='teacher_potho')),
                ('manzil', models.CharField(blank=True, max_length=100, null=True)),
                ('fani', models.ManyToManyField(blank=True, null=True, to='dashboard.Fan')),
                ('useri', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': "O'qituvchilar",
            },
        ),
        migrations.CreateModel(
            name='Kutayotganlar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism_familya', models.CharField(max_length=200)),
                ('telefon', models.CharField(max_length=17)),
                ('manzil', models.CharField(max_length=300)),
                ('qayerdan_keldi', models.CharField(max_length=50)),
                ('pasport', models.ImageField(blank=True, null=True, upload_to='pasport')),
                ('sana', models.DateField(auto_now_add=True)),
                ('bir_oila', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='oila', to='dashboard.talaba')),
                ('dars', models.ManyToManyField(blank=True, null=True, to='dashboard.Fan')),
                ('taklif', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.talaba')),
            ],
            options={
                'verbose_name_plural': 'Kutayotganlar',
            },
        ),
        migrations.AddField(
            model_name='guruh',
            name='kunlari',
            field=models.ManyToManyField(to='dashboard.HaftaKunlari'),
        ),
        migrations.AddField(
            model_name='guruh',
            name='oqituvchi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='guruh',
            name='oquvchi',
            field=models.ManyToManyField(through='dashboard.Azolik', to='dashboard.Talaba'),
        ),
        migrations.CreateModel(
            name='Davomat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sana', models.DateField(auto_now_add=True)),
                ('keldi', models.IntegerField()),
                ('guruh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.guruh')),
                ('oqituvchi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('talaba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.talaba')),
            ],
        ),
        migrations.CreateModel(
            name='Bonus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('takliflar_soni', models.IntegerField(default=0)),
                ('kam_taminlangan', models.BooleanField(default=False)),
                ('kop_fan', models.BooleanField(default=False)),
                ('sana', models.DateField(auto_now_add=True)),
                ('bir_oila', models.ManyToManyField(blank=True, null=True, related_name='birOila', to='dashboard.Talaba')),
                ('talaba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oquvchi', to='dashboard.talaba')),
            ],
        ),
        migrations.AddField(
            model_name='azolik',
            name='guruh',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.guruh'),
        ),
        migrations.AddField(
            model_name='azolik',
            name='talaba',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.talaba'),
        ),
    ]
