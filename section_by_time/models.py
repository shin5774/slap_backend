from django.db import models
from plants_section.models import PlantsSection
from datetime import datetime

def user_directory_path(instance,filename):
    name=str(datetime.now().strftime("%Y-%m-%d-%H"))+'h_input_image.jpg'
    return 'image/{0}/{1}/{2}/{3}'.format(
        instance.section.farm.user.id,instance.section.farm.name,instance.section.name,name)

class SectionByTime(models.Model):
    id=models.AutoField(primary_key=True)
    date=models.DateTimeField(default=datetime.now)
    image=models.ImageField(upload_to=user_directory_path,null=True)
    status=models.CharField(max_length=1, default='0')
    section=models.ForeignKey(PlantsSection,on_delete=models.CASCADE,null=True)

    class Meta:
        managed = True
        db_table = "section_by_time"
'''
    def __str__(self):
        return "그룹명 : "+self.name+"상태 : "+self.status
'''