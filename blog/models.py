from io import BytesIO
from pathlib import Path
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from utils.models import TimestampModel

from PIL import Image

User=get_user_model()
class Blog(TimestampModel):
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
    image=models.ImageField(verbose_name='이미지',null=True,blank=True,upload_to='blog/%Y-%m-%d')
    thumbnail=models.ImageField(verbose_name='썸네일',null=True,blank=True,upload_to='blog/thumbnail/%Y-%m-%d')
    def __str__(self):
        return f'[{self.get_category_display()}]{self.title[:10]}'
    
    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'blog_pk':self.pk})
    
    def get_thumbnail_image(self):
        if self.thumbnail:
            return self.thumbnail.url
        elif self.image:
            return self.image.url
        return None
    
    def save(self,*args,**kwargs):#DB에 저장하기 전에 할 작업을 추가하기 위해 super().save()를 오버라이딩
        if not self.image:
            return super().save(*args,**kwargs)
        image=Image.open(self.image)
        image.thumbnail((300,300))
        image_path=Path(self.image.name)
        thumbnail_name=image_path.stem #/blog/untitled.png => untitled
        thumbnail_extension=image_path.suffix.lower() # /blog/untitled.png => .png
        thumbnail_filename=f'{thumbnail_name}_thumb{thumbnail_extension}'#/blog/untitled.png => untitled_thumb.png
        if thumbnail_extension in ['.jpg','.jpeg']:
            file_type='JPEG'
        elif thumbnail_extension =='.gif':
            file_type='GIF'
        elif thumbnail_extension=='.png':
            file_type='PNG'
        else:
            return super().save(*args,**kwargs)
        temp_thumb=BytesIO()
        image.save(temp_thumb,file_type)
        temp_thumb.seek(0)
        self.thumbnail.save(thumbnail_filename,temp_thumb,save=False)
        temp_thumb.close()
        return super().save(*args,**kwargs)
        
    class Meta:
        verbose_name='블로그'
        verbose_name_plural='블로그 목록'
        
class Comment(TimestampModel):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    content= models.CharField('본문',max_length=255)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.blog.title} 댓글"
    class Meta:
        verbose_name='댓글'
        verbose_name_plural='댓글 목록'
        ordering=('-created_at','id')