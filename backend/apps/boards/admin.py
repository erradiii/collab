from django.contrib import admin
from .models import Board, Column, Task, Comment, Label

admin.site.register(Board)
admin.site.register(Column)
admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(Label)
