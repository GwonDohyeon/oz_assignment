"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import redirect, render
from django.urls import include, path, reverse
from blog.views import (blog_list,blog_detail,blog_create,blog_update,blog_delete,
                        BlogListView,BlogDetailView,BlogCreateView,BlogUpdateView,BlogDeleteView)
from member.views import signup,login
from django.views.generic import TemplateView,RedirectView
from django.views import View
from django.conf import settings
from django.conf.urls.static import static
"""
class AboutView(TemplateView):
    template_name='about.html'
    
class TestView(View):# View는 아무 기능 없는 view로 template연결해주는 것은 아니고 특정 method의 요정이 들어왔을 때 처리할 일을 메소드에 정의
    def get(self,request):
        return render(request,'test_get.html')
        
    def post(self,request):
        return render(request,'test_post.html')

"""

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('blog/<int:id>/',blog_detail,name='blog_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('',blog_list,name='blog_list'),
    path('signup/',signup,name='signup'),
    path('login/',login,name='login'),
    #path('create/',blog_create,name='blog_create'),
    #path('<int:pk>/update/',blog_update,name='blog_update'),
    #path('<int:pk>/delete/',blog_delete,name='blog_delete'),
    # path('about/',TemplateView.as_view(template_name='about.html'),name='about'),
    # path('about/',AboutView.as_view(),name='about'),
    # path('redirect/',RedirectView.as_view(pattern_name='about'),name='redirect'),
    # path('redirect2/',lambda req: redirect(reverse('about'))),
    # path('test/',TestView.as_view(),name='test'),
    path('',include('blog.urls')),
    path('summernote/',include('django_summernote.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)