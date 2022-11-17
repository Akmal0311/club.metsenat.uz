from rest_framework import serializers
from . import models


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sponsor
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = '__all__'


class OTMSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OTM
        fields = '__all__'


class SponsorPayForStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SponsorPayForStudent
        fields = '__all__'
