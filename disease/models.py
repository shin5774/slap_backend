from django.db import models

class Disease(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    explain = models.CharField(max_length=512, null=False)

    class Meta:
        managed = True
        db_table = "disease"

    def __str__(self):
        return "병명 : "+self.name