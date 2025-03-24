from django import forms
from blog.models import Blog,Comment
from django_summernote.widgets import SummernoteWidget
class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=('category','title','image','content',)
        widgets={
            'content':SummernoteWidget()
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('content',)#어떤필드를 입력할 것인가
        widgets={#input태그의 속성 설정
            'content':forms.TextInput(attrs={'class':'form-control'})
        }
        labels={
            'content':'댓글'#models.py의 Comment.content.name='본문' 대신 '댓글'로 표현
        }