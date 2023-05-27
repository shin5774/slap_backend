from rest_framework import serializers
from .models import SectionByTime

class SectionByTimeSerializer(serializers.ModelSerializer) :
    class Meta :
        model = SectionByTime
        fields = '__all__'