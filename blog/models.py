from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User=get_user_model()
class Blog(models.Model):
    CATEGORY_CHOICES = [
        ("travel", "여행"),
        ("ect", "기타"),
        ("pet", "반려동물"),
        ("anniversary", "기념일"),
    ]
    
    title = models.CharField('제목', max_length=100)
    content = models.TextField('본문')
    category = models.CharField('카테고리', max_length=20, choices=CATEGORY_CHOICES,default='ect')
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='수정일', auto_now=True)
    
    def __str__(self):
        return f'[{self.get_category_display()}]{self.title[:10]}'
    
    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})
    
    class Meta:
        verbose_name='블로그'
        verbose_name_plural='블로그 목록'
