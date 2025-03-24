from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect, render,get_object_or_404
from django.urls import reverse, reverse_lazy
from blog.models import Blog,Comment
from blog.forms import BlogForm,CommentForm
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
        'object_list':page_object.object_list,
        'page_obj':page_object,
    }
    response=render(request,'blog_list.html',context)
    response.set_cookie('visits',visits)#cookie는 브라우저에 저장하기 때문에 보안 이슈가 있는 정보는 저장하지 않음
    return response

def blog_detail(request,id):
    blog=get_object_or_404(Blog,id=id)
    context={
        'blog':blog,
        'test':'FBV',
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
    return render(request,'blog_form.html',context)

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
    return render(request,'blog_form.html',context)

@login_required()
@require_http_methods(['POST'])# 특정 method만 받을 수 있다.
def blog_delete(request,pk): 
    blog=get_object_or_404(Blog,pk=pk,author=request.user)
    
    #if request.method != 'POST':
    #    raise Http404
    blog.delete()
    return redirect(reverse('blog_list'))

###################################################################
#CBV
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class BlogListView(ListView):
    # model=Blog 는 queryset=Blog.objects.all()를 의미 
    #queryset=Blog.objects.all().order_by('id')
    queryset=Blog.objects.all()
    template_name='blog_list.html'
    paginate_by=5
    ordering=('id',)
    
    def get_queryset(self):
        queryset=super().get_queryset()#쿼리 조건 집어넣는 MultipleObjectMixin클래스의 메소드 함수
        
        q=self.request.GET.get('q') #blog_list.html의 17번째 줄 input태그의 name='q'이기 때문에 request.GET.get('q')인 것
        #만략 검색어가 있다면
        if q:
            queryset=queryset.filter(
                Q(title__icontains=q)|
                Q(content__icontains=q)
            )
        return queryset

"""
class BlogDetailView(DetailView):
    model=Blog
    queryset=Blog.objects.all().prefetch_related('comment_set','comment_set__author')
    template_name='blog_detail.html'
    def get_object(self, queryset = None):
        object=super().get_object(self.queryset)
        #object=self.model.objects.get(pk=self.kwargs.get('pk')) <int:pk>를 self.kwargs.get('pk')로 받아오기
        return object
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['test']='CBV'
        context['comment_form']=CommentForm()
        return context
    def post(self,*args,**kwargs):
        comment_form=CommentForm(self.request.POST)#commentform을 requset data를 사용해서 만듦
        if not comment_form.is_valid():
            self.object=self.get_object()
            context=self.get_context_data(object=self.object)
            #위 두 줄의 작업은 get()에서 해준다.
            context['comment_form']=comment_form#입력이 유효하지않다고 판명된다면 입력했던 값 그대로 보여주기
            return self.render_to_response(context)
        if not self.request.user.is_authenticated:
            raise Http404
        comment=comment_form.save(commit=False)
        comment.blog=self.get_object()
        comment.author=self.request.user
        comment.save()
        return HttpResponseRedirect(reverse_lazy('blog:detail',kwargs={'pk':self.kwargs['pk']}))
"""

class BlogDetailView(ListView):
    model=Comment
    queryset=Blog.objects.all().prefetch_related('comment_set','comment_set__author')
    template_name='blog_detail.html'
    paginate_by=10
    def get(self,request,*args,**kwargs):#dispatch때 가장 먼저 실행되는 함수 get 오버라이딩으로 self.object에 Blog 담아두기
        self.object=get_object_or_404(Blog,pk=kwargs.get('blog_pk'))
        return super().get(request,*args,**kwargs)
    def get_queryset(self):
        return self.model.objects.filter(blog=self.object).prefetch_related('author')
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['comment_form']=CommentForm()
        context['blog']=self.object
        return context
class BlogCreateView(LoginRequiredMixin,CreateView):#LoginRequiredMixin은 FBV의 @login_required()와 똑같은 기능을 수행
    model=Blog
    template_name='blog_form.html'
    form_class=BlogForm
    #fields=('title','content','category')#입력받을 필드 지정-->따로 BlogForm작성 불필요 django가 알아서 ModelForm작성해 준다.
    #success_url=reverse_lazy('cd_blog_detail.html') #정적 리디렉션 시 사용
    def form_valid(self, form):#폼이 유효할 때 실행됨
        self.object=form.save(commit=False)#객체를 먼저 생성하되, DB에는 저장하지 않음
        self.object.author=self.request.user#author필드 추가
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    def get_success_url(self):#동적 리디렉션 시 사용
        return reverse_lazy('blog:detail', kwargs={'blog_pk': self.object.pk})  # 작성한 블로그 상세 페이지로 이동
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['sub_title']='작성'
        context['btn_name']='생성'
        return context

class BlogUpdateView(LoginRequiredMixin,UpdateView):
    model=Blog
    template_name='blog_form.html'
    form_class=BlogForm
    #fields=('title','content','category')
    #author 필드 추가할게 아니라서 form_valid는 필요 없다.
    def get_success_url(self):#동적 리디렉션 시 사용
        return reverse_lazy('blog:detail', kwargs={'blog_pk': self.object.pk})  # 수정한 블로그 상세 페이지로 이동
    def get_queryset(self):
        queryset=super().get_queryset()
        if self.request.user.is_superuser:
            return queryset
        queryset=queryset.filter(author=self.request.user)
        return queryset
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['sub_title']='수정'
        context['btn_name']='수정'
        return context
class BlogDeleteView(LoginRequiredMixin,DeleteView):
    model=Blog
    def get_queryset(self):
        queryset=super().get_queryset()
        if self.request.user.is_superuser:
            return queryset
        return queryset.filter(author=self.request.user)
    #delete같은 경우 redirect를 model.py의 get_absolute_url의 blog_detail,kwargs={'pk':self.pk}로 하면 안됨(이미 삭제된 객체이므로)
    def get_success_url(self):
        return reverse_lazy('blog:list')
class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        return reverse_lazy('blog:detail', kwargs={'blog_pk': self.object.blog.pk})

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser:
            return queryset
        return queryset.filter(author=self.request.user)
class CommentCreateView(LoginRequiredMixin,CreateView):
    model=Comment
    form_class=CommentForm
    
    def get(self,*args,**kwargs):
        raise Http404
    
    def get_blog(self):
        pk=self.kwargs['blog_pk']#self.kwargs['pk']는 Blog의 pk가 아니라 Comment의 pk
        blog=get_object_or_404(Blog,pk=pk)
        return blog
    def form_valid(self, form):
        blog=self.get_blog()
        self.object=form.save(commit=False)
        self.object.author=self.request.user
        self.object.blog=blog
        self.object.save()
        return HttpResponseRedirect(reverse_lazy('blog:detail', kwargs={'blog_pk': self.object.blog.pk}))

    