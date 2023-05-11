from rest_framework import serializers
from .models import PlantsSection

class PlantsSectionSerializer(serializers.ModelSerializer) :
    user=serializers.ReadOnlyField(source = 'user.id')
    class Meta :
        model = PlantsSection
        fields = '__all__'