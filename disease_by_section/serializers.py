from rest_framework import serializers
from .models import DiseaseBySection

class DiseaseBySectionSerializer(serializers.ModelSerializer) :
    class Meta :
        model = DiseaseBySection
        fields = '__all__'