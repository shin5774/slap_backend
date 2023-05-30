import os
from datetime import datetime

from user.models import User
from .models import SectionByTime
from plants_section.models import PlantsSection
from farm.models import Farm
from disease.models import Disease
from disease_by_section.models import DiseaseBySection

from rest_framework.response import Response
from .serializers import SectionByTimeSerializer
from rest_framework import viewsets,status
from rest_framework.decorators import action
from django.http import JsonResponse
from django.core import serializers

import tensorflow as tf
from yolov5 import strawberry_yolo

leaf_classification = tf.keras.models.load_model('yolov5/res101.h5')

class SectionByTimeListAPI(viewsets.ModelViewSet):
    queryset = SectionByTime.objects.all()
    serializer_class = SectionByTimeSerializer

    #삭제 수행안됨
    #[delete] farm/{id}/
    def perform_destroy(self, instance):
        #instance.is_delete = '1'
        instance.save()

    @action(detail=False, methods=['POST'])
    def section_update(self,request):
        #session에 farm정보를 넣을수 있으면 좋음. 근데 이게 될까?
        data=[]

        user = User.objects.get(id=request.session['id'])
        farm = Farm.objects.get(user=user, name=request.data['name'])
        #user = User.objects.get(id='user1')
        #farm = Farm.objects.get(user=user, name='f1')
        sections=PlantsSection.objects.filter(farm=farm)

        images = request.FILES.getlist('image')
        time=str(datetime.now().strftime("%Y-%m-%d-%H"))

        farm_disease=False
        leaf_detect_fail=[]

        #이미지가 section수 만큼 들어오지 않았을경우의 예외처리
        if len(sections) != len(images):
            return Response({"msg":"이미지가 section 수에 맞게 들어오지 않았습니다."})

        for i in range(len(sections)):
            section=sections[i]
            image=images[i]
            #save 하고 update 해야할듯?

            #savedsad
            sbt=SectionByTime()
            sbt.image=image
            sbt.section=section
            sbt.save()

            #using yolo
            file_path='media/image/{0}/{1}/{2}/'.format(user.id, farm.name,section.name)
            weights='yolov5/leaf_detect.pt'
            output_img, state = strawberry_yolo.detection(weights, file_path,time+"h_")

            if status == 0:
                leaf_detect_fail.append(i+1)
                continue

            # disease detection
            disease_list=[False,False,False]
            section_disease=False
            N=strawberry_yolo.leaf_count(file_path)
            classification_result = strawberry_yolo.classification(leaf_classification, N, file_path)

            for j in range(N):
                if classification_result[j]!=3:
                    disease_list[classification_result[j]]=True

            for k in range(3):
                #disease 데이터 베이스 저장
                if disease_list[k]:
                    disease=Disease.objects.get(id=k+1)
                    #disease_by_section 저장
                    dbs=DiseaseBySection()
                    dbs.cur_section=sbt
                    dbs.disease=disease
                    dbs.save()
                    section_disease=True

            if section_disease:
                # sbt update
                sbt.status=1
                sbt.save()
                farm_disease=True

                #section update
                if section.status!='1':
                    section.status='1'
                    section.save()

            elif section.status=='1':
                section.status='0'
                section.save()

            for j in range(N):
                os.remove(os.path.join(file_path,'leaf_{0}.jpg'.format(j+1)))

            os.remove(os.path.join(file_path,'output_image.jpg'))
            context = {'id': sbt.id, 'image_url': sbt.image.url, 'section_id': sbt.section.id}

            if section_disease:
                context['is_disease'] = 1
                context['disease']=[]
                for cd in range(3):
                    if disease_list[cd]:
                        ccd = Disease.objects.get(id=cd + 1)
                        context['disease'].append({"name": ccd.name, "explain": ccd.explain})
            else:
                context['is_disease'] = 0

            data.append(context)
        if farm_disease:
            farm.status='1'
        else:
            farm.status='0'

        farm.save()

        if len(leaf_detect_fail)!=0:
            return Response({"msg": "save success but not leaf detected section exist"})

        return JsonResponse(data,safe=False)
        #return Response({"msg":"save success"})

    @action(detail=False,methods=['GET'])
    def latest_section(self,request):
        context={}
        section=PlantsSection.objects.get(id=request.data['section_id'])
        sbt=SectionByTime.objects.filter(section=section).latest('date')

        serialized_data = serializers.serialize('json', [sbt])

        try:
            is_disease=DiseaseBySection.objects.get(cur_section=sbt)
            disease=Disease.objects.get(id=is_disease.dissease.id)
            context['is_disease']=1
            context['disease']=disease.name
            context['explain']=disease.explain
        except DiseaseBySection.DoesNotExist:
            context['is_disease']=0

        return Response({"seciton":serialized_data,"disease":context})