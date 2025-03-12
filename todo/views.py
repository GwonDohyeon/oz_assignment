from django.shortcuts import render,get_object_or_404
from todo.models import Todo

# Create your views here.
def todo_list(request):
    todo_list=Todo.objects.all()
    context={'todo_list':todo_list}
    return render(request,'todo_list.html',context)
def todo_info(request,todo_id):
    todo=get_object_or_404(Todo,pk=todo_id)
    info = {
            'title': todo.title,
            'description': todo.description,
            'start_date': todo.start_date,
            'end_date': todo.end_date,
            'is_completed': todo.is_completed,
        }
    context={'data':info}
    return render(request,'todo_info.html',context)
