from django.shortcuts import render,get_object_or_404
from blog.models import Blog

def blog_list(request):
    blogs=Blog.objects.all()
    
    visits=int(request.COOKIES.get('visits',0))+1
    
    request.session['count']=request.session.get('count',0)+1
    
    context={
        'blogs':blogs,
        'count':request.session['count']
    }
    response=render(request,'blog_list.html',context)
    response.set_cookie('visits',visits)#cookie는 브라우저에 저장하기 때문에 보안 이슈가 있는 정보는 저장하지 않음
    return response
def blog_detail(request,id):
    blog=get_object_or_404(Blog,id=id)
    context={
        'blog':blog
    }
    return render(request,'blog_detail.html',context)