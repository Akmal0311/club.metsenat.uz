from django.db import models


class Sponsor(models.Model):

    STATUS = (
        ('NEW', 'new'),
        ('MODERATION', 'moderation'),
        ('CONFIRMED', 'confirmed'),
        ('CANCELED', 'canceled')
    )

    fish = models.CharField(max_length=111, blank=False)
    phone_number = models.CharField(max_length=17, blank=False)
    payment = models.IntegerField()
    juridical = models.BooleanField(default=False)
    organization = models.CharField(max_length=333, blank=True)

    spent_amount = models.IntegerField(default=0, blank=True)
    date = models.DateField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=33, choices=STATUS, default='NEW')

    def __str__(self):
        return self.fish


class Student(models.Model):

    STUDENT_TYPE = (
        ('BACHELOR', 'bachelor'),
        ('MASTER', 'master'),
        ('PhD', 'phd')
    )

    fish = models.CharField(max_length=111, blank=False)
    phone_number = models.CharField(max_length=17, blank=False)
    ihe = models.ForeignKey('IHE', on_delete=models.CASCADE)
    student_type = models.CharField(max_length=10, choices=STUDENT_TYPE, default=STUDENT_TYPE[0][0])
    contract_amount = models.IntegerField()
    date = models.DateField(auto_now_add=True, blank=True)

    allocated_amount = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.fish


class IHE(models.Model):

    name = models.CharField(max_length=333, blank=False)

    def __str__(self):
        return self.name


class SponsorPayForStudent(models.Model):

    sponsor = models.ForeignKey('Sponsor', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return "sponsor: {}, student: {}, amount: {}".format(self.sponsor, self.student, self.amount)

