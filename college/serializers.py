from rest_framework import serializers
from .models import College, AdmissionStats, Scores, Student


class CollegeSerializer(serializers.ModelSerializer):

    class Meta:
        model = College
        fields = ('name', 'ipeds', 'color')

class AdmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = College
        fields = '__all__'
