from django.db import models


class BaseModel(models.Model):

    created_at = models.DateTimeField("Kiritilgan sana", auto_now_add=True)
    updated_at = models.DateTimeField("O'zgartirilgan sana", auto_now=True)

    class Meta:
        abstract = True


class Sponsor(BaseModel):

    STATUS = (
        ('NEW', 'new'),
        ('MODERATION', 'moderation'),
        ('CONFIRMED', 'confirmed'),
        ('CANCELED', 'canceled')
    )

    fish = models.CharField(max_length=111, blank=False, verbose_name="Familya Ism Sharifi")
    phone_number = models.CharField(max_length=17, blank=False, verbose_name="Telfon raqami")
    payment = models.IntegerField(verbose_name="Homiylik summasi")
    juridical = models.BooleanField(default=False, verbose_name="Yuridik")
    organization = models.CharField(max_length=333, blank=True, verbose_name="Tashkilot nomi")
    spent_amount = models.IntegerField(default=0, blank=True, verbose_name="Sarflangan summasi")
    status = models.CharField(max_length=33, choices=STATUS, default='NEW', verbose_name="Holati")

    def __str__(self):
        return self.fish

    class Meta:
        verbose_name = "Homiy "
        verbose_name_plural = "1. Homiylar"


class Student(BaseModel):

    STUDENT_TYPE = (
        ('BACHELOR', 'bachelor'),
        ('MASTER', 'master'),
        ('PhD', 'phd')
    )

    fish = models.CharField(max_length=111, blank=False, verbose_name="Familya Ism Sharifi")
    phone_number = models.CharField(max_length=17, blank=False, verbose_name="Telefon raqami")
    otm = models.ForeignKey('OTM', on_delete=models.CASCADE, verbose_name="Oliy Ta'lim Muassasasi")
    student_type = models.CharField(max_length=10, choices=STUDENT_TYPE, default=STUDENT_TYPE[0][0], verbose_name="Talaba turi")
    contract_amount = models.IntegerField(verbose_name="Kontrakt summasi")
    allocated_amount = models.IntegerField(default=0, blank=True, verbose_name="Ajratilgan summasi")

    def __str__(self):
        return self.fish

    class Meta:
        verbose_name = "Talaba "
        verbose_name_plural = "2. Talabalar"


class OTM(BaseModel):

    name = models.CharField(max_length=333, blank=False, verbose_name="Nomi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Oliy Ta'lim Muassasasi "
        verbose_name_plural = "3. Oliy Ta'lim Muassasalari"


class SponsorPayForStudent(BaseModel):

    sponsor = models.ForeignKey('Sponsor', on_delete=models.CASCADE, verbose_name="Homiy")
    student = models.ForeignKey('Student', on_delete=models.CASCADE, verbose_name="Talaba")
    amount = models.IntegerField(verbose_name="Summa")

    def __str__(self):
        return "sponsor: {}, student: {}, amount: {}".format(self.sponsor, self.student, self.amount)

    class Meta:
        verbose_name = "Homiy summasi talaba uchun "
        verbose_name_plural = "4. Homiylar summasi talabalar uchun"
