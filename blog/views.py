from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import redirect, render,get_object_or_404
from django.urls import reverse
from blog.models import Blog
from blog.forms import BlogForm
from django.db.models import Q
from django.views.decorators.http import require_http_methods

def blog_list(request):
    blogs=Blog.objects.all().order_by('id')
    
    q=request.GET.get('q')
    if q:
        blogs=blogs.filter(
            Q(title__icontains=q),
            Q(content__icontains=q),
        )
        
    paginator=Paginator(blogs,5)
    page=request.GET.get('page')#url에 있는 query string을 가져오는 함수
    page_object=paginator.get_page(page)
    
    visits=int(request.COOKIES.get('visits',0))+1
    
    request.session['count']=request.session.get('count',0)+1
    
    context={
        #'blogs':blogs,
        'count':request.session['count'],
        'page_object':page_object,
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

@login_required()
def blog_create(request):
    form=BlogForm(request.POST or None)
    if form.is_valid():
        blog=form.save(commit=False)
        blog.author=request.user
        blog.save()
        return redirect(reverse('blog_detail',kwargs={'id':blog.pk}))
    
    context={
        'form':form,
    }
    return render(request,'blog_create.html',context)

@login_required()
def blog_update(request,pk): 
    """
    blog=get_object_or_404(Blog,pk=pk)
    if request.user != blog.author:
        raise Http404
    """
    blog=get_object_or_404(Blog,pk=pk,author=request.user)
    form=BlogForm(request.POST or None,instance=blog)
    if form.is_valid():
        blog=form.save()
        return redirect(reverse('blog_detail',kwargs={'id':blog.pk}))
    context={
        'form':form,
    }
    return render(request,'blog_update.html',context)

@login_required()
@require_http_methods(['POST'])# 특정 method만 받을 수 있다.
def blog_delete(request,pk): 
    blog=get_object_or_404(Blog,pk=pk,author=request.user)
    
    #if request.method != 'POST':
    #    raise Http404
    blog.delete()
    return redirect(reverse('blog_list'))