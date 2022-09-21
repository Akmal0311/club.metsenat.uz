from rest_framework import serializers
from .models import *


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class IHESerializer(serializers.ModelSerializer):
    class Meta:
        model = IHE
        fields = '__all__'


class SponsorPayForStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorPayForStudent
        fields = '__all__'




