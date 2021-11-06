from django.shortcuts import render
from typing import Dict

context = {
           'title_index':'Это главная страница проекта Yatube',
           'title_groups':'Здесь будет информация о группах проекта Yatube'
          }


def index(request):
    """Главная страница."""
    template = 'posts/index.html'
    return render(request, template, context)

def group_posts(request):
    """Cтраница  публикаций."""
    template = 'posts/group_list.html'
    return render(request, template, context)