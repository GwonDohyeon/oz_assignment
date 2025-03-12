from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,Http404
from bookmark.models import Bookmark
# Create your views here.
def bookmark_list(request):
    bookmarks=Bookmark.objects.all()#select * from bookmark
    context={
        'bookmarks':bookmarks
    }
    return render(request,'bookmark_list.html',context)

def bookmark_detail(request,pk):
    """
    try:
        bookmark=Bookmark.objects.get(id=pk)
    except:
        raise Http404
    """
    bookmark=get_object_or_404(Bookmark,pk=pk)
    context={'bookmark':bookmark}
    return render(request,'bookmark_detail.html',context)