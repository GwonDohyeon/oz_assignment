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
from django.urls import path
from django.http import HttpResponse,Http404
from django.shortcuts import render
from bookmark.views import bookmark_detail, bookmark_list
from todo.views import todo_list,todo_info
from fake_db import user_db

_db = user_db

def user_list(request):
    names = [{'id': key, 'name': value['이름']} for key, value in _db.items()]
    return render(request, 'user_list.html', {'data': names})


def user_info(request, user_id):
    if user_id > len(_db):
        raise Http404('User not found')
    info = _db[user_id]
    return render(request, 'user_info.html', {'data': info})


movie_li=[
    {'title':'파묘','direct':'장재현'},
    {'title':'웡카','direct':'폴 킹'},
    {'title':'듄','direct':'드니'},
    {'title':'시민덕희','direct':'박영주'},
]


def index(request):
    return HttpResponse('hello')
def book_list(request):
    book_text=''
    for i in range(0,10):
        book_text+=f'book {i}<br>'
    return HttpResponse(book_text)
def book(request,num):
    book_text=f'book {num}<br>'
    return HttpResponse(book_text)
def lang(request,lang):
    return HttpResponse(f'<h1>{lang}언어 페이지')


def movies(request):
    """movie_title=[movie['title'] for movie in movie_li]
    text=''
    for i,t in enumerate(movie_title):
        text+=f'<a href="/movie/{i}">{t}</a><br>'
    return HttpResponse(text)
    
    movie_title=[
        f'<a href="/movie/{i}">{movie["title"]}</a>' 
        for i, movie in enumerate(movie_li)
        ]
    text='<br>'.join(movie_title)
    return HttpResponse(text)"""
    return render(request,template_name='movies.html',context={'movie_list':movie_li})

def movies_detail(request,i):
    """
    if i > len(movie_li)-1:
        raise Http404 # 400대 오류는 사용자 잘못, 500대 오류는 서버쪽 잘못
    movie=movie_li[i]
    return HttpResponse(f"<h1>{movie['title']}</h1> <p>감독: {movie['direct']}</p>")
    """
    if i > len(movie_li)-1:
        raise Http404 # 400대 오류는 사용자 잘못, 500대 오류는 서버쪽 잘못
    #movie=movie_li[i]
    context={'movie_list':movie_li,'index':i}
    return render(request,'movie.html',context)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',index),
    #path('book_list/',book_list),
    #path('book_list/<int:num>',book),
    #path('lang/<str:lang>',lang),
    #path('movie/<int:i>',movies_detail),
    #path('movie/',movies),
    #path('users/', user_list, name='user_list'),
    #path('users/<int:user_id>/', user_info, name='user_info'),
    path('bookmark/',bookmark_list),#모든 경로는 '/'를 붙여야한다, 안붙이면 '/url/'로 redirection수행
    path('bookmark/<int:pk>/',bookmark_detail),
    path('todo/',todo_list),
    path('todo/<int:todo_id>/',todo_info),
]
