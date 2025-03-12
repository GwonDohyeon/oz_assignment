from django.contrib import admin
from todo.models import Todo

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display=['title','is_completed','end_date','created_at']#목록에 보여줄 필드
    list_display_links=['title']#클릭으로 상세 페이지 이동할 필드
    list_filter=['is_completed','start_date','end_date']#필터링 가능한 필드
    search_fields=['title','start_date','end_date']#검색 가능 필드
    ordering=['-modified_at']#정렬 기준 '-'는 최신순으로 보겠다는 의미
    readonly_fields = ['created_at', 'modified_at']#읽기 전용 필드
    #상세페이지 설정
    fieldsets=[
        (
            None,
            {
                'fields':['title','is_completed','created_at','modified_at'],
            },
        ),
        (
            '기한',
            {
                'fields':['start_date','end_date'],
            }
        ),
        (
            '내용',
            {
                'fields':['description']
            }
        )
    ]
admin.site.register(Todo,TodoAdmin)