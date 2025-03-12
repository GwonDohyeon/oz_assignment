from django.db import models

# Create your models here.
class Todo(models.Model):
    title=models.CharField(name='title',max_length=50)
    description=models.TextField(name='description')
    start_date=models.DateField(verbose_name='시작일')
    end_date=models.DateField(verbose_name='마감일')
    is_completed=models.BooleanField(name='is_completed',default=False)
    created_at=models.DateTimeField(verbose_name='생성 일시',auto_now_add=True)#auto_now_add는 객체 생성 시 설정
    modified_at=models.DateTimeField(verbose_name='수정 일자',auto_now=True)#auto_now는 Model.save()할 때마다 갱신
    def __str__(self):
        return self.title
    