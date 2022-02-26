from django.shortcuts import render, get_object_or_404
from .models import Post, Board
from django.utils import timezone
from .forms import PostForm, BoardForm
from django.shortcuts import redirect



def board_list(request):
    boards = Board.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'chatboard/board_list.html', {'boards' : boards})


def post_list(request, pk):
    board = get_object_or_404(Board, pk=pk)
    posts = Post.objects.filter(belong = board).order_by('published_date')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.belong = board
            post.save()
            return redirect('post_list', pk=board.pk) 
    else: 
        form = PostForm()
    params = {
        'form' : form,
        'posts' : posts,
    }
    return render(request, 'chatboard/post_list.html', params)


def board_new(request):
    if request.method == "POST":
        form = BoardForm(request.POST) 
        if form.is_valid():
            board = form.save(commit=False)
            board.created_date = timezone.now()
            board.save()
            return redirect('board_list')
    else:
        form = BoardForm()
    
    return render(request, 'chatboard/board_list', {'form': form})



