import os
from datetime import datetime

from user.models import User
from farm.models import Farm

from rest_framework.response import Response
from .serializers import FarmSerializer
from rest_framework import viewsets,status
from rest_framework.decorators import action

class PlantsGroupListAPI(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer

    def create(self, request):
        context={}
        context['name'] = request.data['name']
        context['number']=request.data['number']
        user=User.objects.get(id=request.session['id'])
        dupl_name=self.queryset.filter(user=user,name=context['name'])

        if len(dupl_name) !=0:
            return Response({"msg":"동일한 이름의 농장이 있습니다. 다른 이름을 등록해주세요"})

        str_date=request.data['date']
        date=datetime.strptime(str_date,"%Y-%m-%d")
        context['date']=date
        context['status']=request.data['status']

        serializer=self.get_serializer(data=context)

        serializer.is_valid()
        self.perform_create(serializer)

        return Response(serializer.data)

    #[post] /farm
    def perform_create(self,serializer):
        user=User.objects.get(id=self.request.session['id'])
        os.mkdir("media/image/" + user.id + "/" + self.request.data['name'])
        serializer.save(user=user) 

    #삭제 수행안됨
    #[delete] farm/{id}/
    def perform_destroy(self, instance):
        #instance.is_delete = '1'
        instance.save()

    # [patch] farm/{id}/change_board/
    # 유저 비번 바꾸는거랑 동일한 방식으로 보내면 됨
    @action(detail=True,methods=['PATCH'])
    def change_status(self,request,pk=None):
        farm=self.queryset.get(id=pk)
        status=request.data['status']

        if status=='1':
            farm.status='1'
        else:
            farm.status='0'

        farm.save()

        serializer=self.get_serializer(farm)
        return Response(serializer.data)

    # 위와 동일/ 필요값 name:변경할 이름
    # [patch] farm/{id}/change_name/
    @action(detail=True, methods=['PATCH'])
    def change_name(self, request, pk=None):
        name = request.data['name']
        user = User.objects.get(id=self.request.session['id'])
        exist=self.queryset.filter(user=user,name=name)

        if len(exist) !=0:
            return Response({"msg":"동일한 이름의 농장이 있습니다. 다른 이름을 등록해주세요"})

        farm = self.queryset.get(id=pk)

        os.rename("media/image/" + user.id + "/" + farm.name,"media/image/" + user.id + "/" + name)

        farm.name = name
        farm.save()

        serializer = self.get_serializer(farm)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def user_list(self, request):
        user = User.objects.get(id=request.session['id'])
        user_farm=Farm.objects.filter(user=user)

        serializer=self.get_serializer(user_farm,many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['PATCH'])
    def change_section(self, request, pk=None):
        farm = self.queryset.get(id=pk)
        number=request.data['number']

        if number<0:
            return Response({"msg": "잘못된 섹션수를 입력하였습니다."})

        #섹션수 수정을 위한 코드(섹션 테이블에 데이터 추가 및 삭제를 하는법 의논 필요)

        farm.number = number
        farm.save()

        serializer = self.get_serializer(farm)
        return Response(serializer.data)


