import datetime, os

from plants_section.models import PlantsSection
from section_detail.models import SectionDetail

from farm.models import Farm
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.db import transaction
from rest_framework.response import Response
from .serializers import SectionDetailSerializer
from rest_framework import viewsets,status
from rest_framework.decorators import action

class PlantsDetailListAPI(viewsets.ModelViewSet):
    queryset = SectionDetail.objects.all()
    serializer_class = SectionDetailSerializer

    #필요값: id:게시판 id
    #[post] /section_detail
    def perform_create(self, serializer):
        board=PlantsSection.objects.get(id=self.request.data['board_id'])
        serializer.save(board=board)

    #삭제 처리안됨
    #[delete] /section_detail/{id}
    def perform_destroy(self, instance):
        #instance.is_delete = '1'
        instance.save()

    @action(detail=False, methods=['GET'])
    def disease_leaves(self, request):
        b_id = request.query_params.get('board_id')
        board=PlantsSection.objects.get(id=b_id)
        leaves=SectionDetail.objects.filter(board=board, is_disease='1')

        serializer=self.get_serializer(leaves,many=True)
        return Response(serializer.data)





