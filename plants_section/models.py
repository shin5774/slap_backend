from datetime import datetime
from pytz import timezone

from django.db import models
from user.models import User
from farm.models import Farm
#이미지 저장 경로 지정 함수
def user_directory_path(instance,filename):
    name='input_image.jpg'
    return 'image/{0}/{1}/{2}/{3}'.format(instance.user.id,instance.plant_group.name,instance.plant_group.board_cnt,name)

def user_directory_path_input(instance,filename):
    name='input_image.jpg'
    return 'image/{0}/{1}/{2}/{3}'.format(instance.user.id,instance.plant_group.name,instance.plant_group.board_cnt,name)

def user_directory_path_output(instance,filename):
    name='output_image.jpg'
    return 'image/{0}/{1}/{2}/{3}'.format(instance.user.id,instance.plant_group.name,instance.plant_group.board_cnt,name)

class PlantsSection(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=True)
    date = models.DateTimeField(default=datetime.now)
    input_image = models.ImageField(upload_to=user_directory_path_input,null=True)
    #output_image = models.FileField(upload_to=user_directory_path_output,null=True) #위치 지정해야하는데 나중에 설정해야할듯?
    status = models.CharField(max_length=1, default='0')
    number = models.IntegerField(default=1)
    farm = models.ForeignKey(Farm,on_delete=models.CASCADE,null=True)
    is_delete = models.CharField(max_length=1, default='0')

    class Meta:
        managed = True
        db_table = "plants_section"

    def __str__(self):
        return "제목 : "+self.name