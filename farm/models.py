from django.db import models
from user.models import User
from datetime import datetime

class Farm(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,null=False)
    date = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=1, default='0')
    row = models.IntegerField(default=1)
    column = models.IntegerField(default=1)
    temperature=models.DecimalField(max_digits=5,decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        managed = True
        db_table = "farm"

    def __str__(self):
        return "농장명 : "+self.name+"상태 : "+self.status