from django.db import models

# 게시글(Borad) 모델
class Board(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=64)
    body = models.TextField()

# 댓글(Comment) 모델
class Comment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    board = models.ForeignKey(Board, null=True, blank=True, on_delete=models.CASCADE)