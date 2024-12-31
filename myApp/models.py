from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(id, primary_key=True)
    username = models.CharField("username", max_length=255, default='')
    password = models.CharField("password", max_length=255, default='')
    createTime = models.DateTimeField("创建时间", auto_now_add=True)
    class Meta:
        db_table = "user"

class History(models.Model):
    id = models.AutoField("id", primary_key=True)
    jobId = models.IntegerField("职位ID", max_length=255, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField("收藏次数", default=1)

    class Meta:
        db_table = "history"

