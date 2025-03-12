from django.db import models

# Create your models here.
class Bookmark(models.Model):
    name=models.CharField('이름',max_length=100)
    url=models.URLField('URL')
    created_at=models.DateTimeField(verbose_name='생성일시',auto_now_add=True)
    updated_at=models.DateTimeField(verbose_name='수정일시',auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='북마크'
        verbose_name_plural='북마크 목록'
#python manage.py makemigrations => migration.py파일 생성
#실제 db에는 영향을 주지 않지만 실제db에 넣기 위한 정의를 하는 파일

#python manage.py migrate => migrations 폴더 안에 있는 파일들을 실제 db에 적용