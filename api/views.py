from django.shortcuts import render, get_object_or_404
from . import serializer, models
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from django.db.models import Count


class SponsorView(generics.CreateAPIView):
    queryset = models.Sponsor.objects.all()
    serializer_class = serializer.SponsorSerializer


class SponsorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Sponsor.objects.all()
    serializer_class = serializer.SponsorSerializer


class SponsorListView(generics.ListAPIView):
    queryset = models.Sponsor.objects.all()
    serializer_class = serializer.SponsorSerializer


class StudentView(generics.CreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializer.StudentSerializer


class StudentListView(generics.ListAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializer.StudentSerializer


class StudentDetailView(APIView):
    queryset = models.Student.objects.all()
    serializer_class = serializer.StudentSerializer
    ss_serializer_class = serializer.SponsorPayForStudentSerializer
    sponsor_serializer = serializer.SponsorSerializer

    def get(self, request, student_id):

        student = get_object_or_404(models.Student, pk=student_id)
        student_serializer = self.serializer_class(instance=student)

        s = models.SponsorPayForStudent.objects.all()
        ss_serializer = self.ss_serializer_class(instance=s,  many=True)

        student_sponsor = list()

        for i in range(len(ss_serializer.data)):
            a = ss_serializer.data[i]

            if int(a['student']) == student_id:
                res = models.Sponsor.objects.get(id=a['sponsor'])
                data = {
                    'id': res.id,
                    'fish': res.fish,
                    'amount': a['amount']
                }
                student_sponsor.append(data)

        data = {
            'student:': student_serializer.data,
            'student sponsors:': student_sponsor
        }

        return Response(data=data, status=status.HTTP_200_OK)

    def delete(self, request, student_id):
        students = models.Student.objects.all()
        for i in range(len(students)):
            student = students[i]

            if student.id == student_id:
                student.delete()

        return Response(data={"data": "successfully"}, status=status.HTTP_200_OK)

    def put(self, request, student_id):
        data = request.data

        print(data)

        student = models.Student.objects.get(id=student_id)
        student.fish = data['fish']
        student.phone_number = data['phone_number']
        student.student_type = data['student_type']
        student.contract_amount = data['contract_amount']
        student.__otm = data['otm']

        student.save()

        return Response(data={"data": "successfully"}, status=status.HTTP_200_OK)


class SponsorPayForStudentView(generics.CreateAPIView):
    queryset = models.SponsorPayForStudent.objects.all()
    serializer_class = serializer.SponsorPayForStudentSerializer

    def post(self, request, student_id, *args, **kwargs):
        data = request.data
        amount = data['amount']

        sponsors = models.Sponsor.objects.all()
        students = models.Student.objects.all()
        sponsor_pay_for_student = models.SponsorPayForStudent.objects.all()
        sponsor_bool = True
        student_bool = True
        sponsor = models.Sponsor
        student = models.Student
        for i in range(len(sponsors)):
            a = sponsors[i]
            if a.id == data['sponsor']:
                sponsor_bool = False
                sponsor = sponsors[i]
        for i in range(len(students)):
            a = students[i]
            if a.id == student_id:
                student_bool = False
                student = students[i]

        if sponsor_bool:
            return Response(data={'error': 'Sponsor Not Found'}, status=status.HTTP_404_NOT_FOUND)

        if student_bool:
            return Response(data={'error': 'Student Not Found'}, status=status.HTTP_404_NOT_FOUND)

        for i in range(len(sponsor_pay_for_student)):
            a = sponsor_pay_for_student[i]
            if a.student.id == student_id and a.sponsor.id == data['sponsor']:
                return Response(data={'error': 'Sponsor bu talabaga oldin pul otkazgan. eltimos sponsor tahrirlash dan summani qo`shing'})
        if sponsor.payment < amount:
            return Response(data={'error': 'Sponsor hisobida yetarli pul mavjud emas!   Sponsor hisobi: {} UZS   To`lanayotgan summa: {} UZS'.format(sponsor.payment, amount)}, status=status.HTTP_400_BAD_REQUEST)

        if student.allocated_amount >= student.contract_amount:
            return Response(data={'error': 'Talaba hisobiga to`lgan! boshqa pul o`tkazib bo`lmaydi.  Talaba hisobi: {} UZS   So`ralgan summa: {} UZS'.format(student.allocated_amount, student.contract_amount)}, status=status.HTTP_400_BAD_REQUEST)

        if student.allocated_amount+amount > student.contract_amount:
            return Response(data={'error': 'Talaba hisobiga so`ralgan summadan ortiq o`tkazib bo`lmaydi.    Siz maksimum o`tkazishingiz mumkin bo`lgan summa: {} UZS'.format(student.contract_amount-student.allocated_amount)}, status=status.HTTP_400_BAD_REQUEST)

        sponsor.payment -= amount
        sponsor.spent_amount += amount
        student.allocated_amount += amount

        sponsor.save()
        student.save()

        models.SponsorPayForStudent.objects.create(
            sponsor=sponsor,
            student=student,
            amount=amount
        )

        return Response(data={"data": "successfully"}, status=status.HTTP_200_OK)


class EditSponsorView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.SponsorPayForStudent.objects.all()
    serializer_class = serializer.SponsorPayForStudentSerializer

    def put(self, request, *args, **kwargs):
        data = request.data

        sp = models.SponsorPayForStudent.objects.all()

        for i in range(len(sp)):
            a = sp[i]

            if a.sponsor.id == data['sponsor'] and a.student.id == data['student']:
                old_sp = models.SponsorPayForStudent.objects.get(id=a.id)
                student = models.Student.objects.get(id=a.student.id)
                sponsor = models.Sponsor.objects.get(id=a.sponsor.id)

                if old_sp.amount <= data['amount']:
                    if student.allocated_amount >= student.contract_amount:
                        return Response(data={'error': 'Talaba hisobiga to`lgan! boshqa pul o`tkazib bo`lmaydi.  Talaba hisobi: {} UZS   So`ralgan summa: {} UZS'.format(student.allocated_amount, student.contract_amount)}, status=status.HTTP_400_BAD_REQUEST)

                if sponsor.payment < data['amount']:
                    return Response(data={'error': 'Sponsor hisobida yetarli pul mavjud emas!   Sponsor hisobi: {} UZS   To`lanayotgan summa: {} UZS'.format(sponsor.payment, data['amount'])}, status=status.HTTP_400_BAD_REQUEST)

                student.allocated_amount -= old_sp.amount

                sponsor.payment += old_sp.amount

                sponsor.spent_amount -= old_sp.amount

                if student.allocated_amount + data['amount'] > student.contract_amount:
                    return Response(data={'error': 'Talaba hisobiga so`ralgan summadan ortiq o`tkazib bo`lmaydi.    Siz maksimum o`tkazishingiz mumkin bo`lgan summa: {} UZS'.format(student.contract_amount - student.allocated_amount)}, status=status.HTTP_400_BAD_REQUEST)

                student.allocated_amount += data['amount']

                sponsor.payment -= data['amount']

                sponsor.spent_amount += data['amount']

                a.amount = data['amount']

                student.save()
                sponsor.save()
                a.save()

                return Response(data={"data": "successfully"}, status=status.HTTP_200_OK)

        return Response(data={"error": "bad request"}, status=status.HTTP_400_BAD_REQUEST)


class OTMView(generics.CreateAPIView):
    queryset = models.OTM.objects.all()
    serializer_class = serializer.OTMSerializer


class OTMDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.OTM.objects.all()
    serializer_class = serializer.OTMSerializer


class OTMListView(generics.ListAPIView):
    queryset = models.OTM.objects.all()
    serializer_class = serializer.OTMSerializer


class Dashboard(APIView):

    def get(self, request):

        students = models.Student.objects.all()
        total_paid_amount, total_required_amount = 0, 0

        for i in range(len(students)):
            student = students[i]
            total_paid_amount += student.allocated_amount
            total_required_amount += student.contract_amount

        total_student = models.Student.objects.all().aggregate(id=Count('id'))['id']
        total_sponsor = models.Sponsor.objects.all().aggregate(id=Count('id'))['id']

        return Response(data={"Jami to'langan summa": total_paid_amount,
                        "Jami so'ralgan summa": total_required_amount,
                        "To'lanishi kerak summa": total_required_amount-total_paid_amount,
                        "Homiylar": total_sponsor,
                        "Talabalar": total_student},
                        status=status.HTTP_200_OK)




