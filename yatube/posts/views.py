from django.shortcuts import render, get_object_or_404
from .models import Post, Group

    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]

context = {
           'posts': posts,
           'title_index':'Это главная страница проекта Yatube',
           'title_groups':'Здесь будет информация о группах проекта Yatube',
           'title_icon':'Здесь находяится коллекция иконок проекта Yatube'
          }


def index(request):
    return render(request, 'posts/index.html', context)

def group_posts(request, slug):
    """Cтраница  публикаций."""
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    context1 = {
                'group': group
               }
    return render(request, template, context1)

