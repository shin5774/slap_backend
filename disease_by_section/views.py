from plants_section.models import PlantsSection
from disease.models import Disease
from disease_by_section.models import DiseaseBySection

from farm.models import Farm
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.db import transaction
from rest_framework.response import Response
from .serializers import DiseaseBySectionSerializer
from rest_framework import viewsets,status
from rest_framework.decorators import action

class PlantsByDiseaseListAPI(viewsets.ModelViewSet):
    queryset = DiseaseBySection.objects.all()
    serializer_class = DiseaseBySectionSerializer

    #필요값:board_id:게시판의 id,disease_name:질병명
    #[post] /plants_by_detail/
    def perform_create(self, serializer):
        board=PlantsSection.objects.get(id=self.request.data['board_id'])
        disease=Disease.objects.get(name=self.request.data['disease_name'])
        serializer.save(board=board,disease=disease)
        
    #삭제처리 안됨
    #[delete] /plants_by_detail/{id}
    def perform_destroy(self, instance):
        #instance.is_delete = '1'
        instance.save()



