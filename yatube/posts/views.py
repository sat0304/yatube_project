from django.http import HttpResponse


def index(request):
    """Главная страница."""
    return HttpResponse('Главная страница')

def group_posts(request, slug):
    return HttpResponse(f'Здесь решается судьба мира {slug}')