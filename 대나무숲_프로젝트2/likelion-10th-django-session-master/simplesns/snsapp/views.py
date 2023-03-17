from django.shortcuts import render, redirect, get_object_or_404
from datetime import timezone
from .models import Board, Comment
from django.core.paginator import Paginator

def home(request):
    # Board 넘겨주기
    boards = Board.objects.filter().order_by('-date')

    # 페이지네이션
    paginator = Paginator(boards, 2)
    pagnum = request.GET.get('page')
    boards = paginator.get_page(pagnum)

    return render(request, 'index.html', {'boards': boards})


def new(request):
    return render(request, 'new.html')

def create(request):
    if(request.method == 'POST'):
        board = Board()
        board.title = request.POST['title']
        board.body = request.POST['body']
        board.date = timezone.now()
        board.save()
    return redirect('home')

def detail(request, board_id):
    # Board 넘겨주기
    board_detail = get_object_or_404(Board, pk=board_id)

    # Comment 넘겨주기
    comment_detail = get_object_or_404(Board, pk=board_id)
    
    return render(request, 'detail.html', {'board_detail': board_detail, 'comment_detail' : comment_detail})

def create_comment(request, board_id):
    comment_detail = Comment()
    comment_detail.comment = request.POST['comment']
    comment_detail.date = timezone.now()
    comment_detail.board = get_object_or_404(Board, pk=board_id)
    comment_detail.save()
    return redirect('detail', board_id)