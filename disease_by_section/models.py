from django.db import models
from disease.models import Disease
from plants_section.models import PlantsSection

class DiseaseBySection(models.Model):
    id=models.AutoField(primary_key=True)
    board=models.ForeignKey(PlantsSection, on_delete=models.CASCADE, null=True)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, null=True)

    class Meta:
        managed = True
        db_table = "disease_by_section"
'''
    def __str__(self):
        return "그룹명 : "+self.name+"상태 : "+self.status
'''