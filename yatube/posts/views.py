from django.shortcuts import render, get_object_or_404
from .models import Post, Group

    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    template = 'posts/index.html'
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
        'title_index':'Это главная страница проекта Yatube'
    }
    return render(request, template, context) 


def group_posts(request, slug):
    """Cтраница  публикаций."""
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)

    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
        'title_groups':'Здесь будет информация о группах проекта Yatube'
    }
    return render(request, template, context)
