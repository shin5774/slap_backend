from rest_framework import serializers
from .models import SectionDetail

class SectionDetailSerializer(serializers.ModelSerializer) :
    class Meta :
        model = SectionDetail
        fields = '__all__'