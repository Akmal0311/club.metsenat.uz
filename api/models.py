from django.db import models


class Sponsor(models.Model):

    STATUS = (
        ('Yangi', 'Yangi'),
        ('Moderatsiyada', 'Moderatsiyada'),
        ('Tastiqlangan', 'Tastiqlangan'),
        ('Bekor qilingan', 'Bekor qilingan')
    )

    fish = models.CharField(max_length=111, blank=False)
    phone_number = models.CharField(max_length=17, blank=False)
    payment = models.IntegerField()
    juridical = models.BooleanField(default=False)
    organization = models.CharField(max_length=333, blank=True)

    spent_amount = models.IntegerField(default=0, blank=True)
    date = models.DateField(auto_now_add=True, blank=True)
    statuss = models.CharField(max_length=33, choices=STATUS, default='Yangi')

    def __str__(self):
        return self.fish


class Student(models.Model):

    STUDENT_TYPE = (
        ('Bakalavr', 'Bakalavr'),
        ('Magistr', 'Magister'),
        ('Doktorant', 'Doktorant')
    )

    fish = models.CharField(max_length=111, blank=False)
    phone_number = models.CharField(max_length=17, blank=False)
    otm = models.ForeignKey('OTM', on_delete=models.CASCADE)
    student_type = models.CharField(max_length=10, choices=STUDENT_TYPE, default=STUDENT_TYPE[0][0])
    contract_amount = models.IntegerField()
    date = models.DateField(auto_now_add=True, blank=True)

    allocated_amount = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.fish


class OTM(models.Model):

    name = models.CharField(max_length=333, blank=False)

    def __str__(self):
        return self.name


class SponsorPayForStudent(models.Model):

    sponsor = models.ForeignKey('Sponsor', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return "sponsor: {}, student: {}, amount: {}".format(self.sponsor, self.student, self.amount)

