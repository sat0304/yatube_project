from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    """Таблица, содержащая группы пользователей."""
    title = models.TextField()
    slug = models.SlugField(
                            unique=True, 
                            max_length=100, 
                            default='title'
                            )
    description = models.TextField()

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    """Таблица, содержащая сообщения (посты) пользователей."""
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
                               User,
                               on_delete=models.CASCADE,
                               related_name='posts_all'
                               )
    group = models.ForeignKey(
                              Group,
                              blank=True,
                              null=True,
                              on_delete=models.CASCADE
                              )