from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20)
    num = models.CharField(max_length=14)
    some_blank = models.TextField(blank=True)
    some_null = models.TextField(null=True)

    @staticmethod
    def init(count=2000, locale='en'):
        from elizabeth import Personal, Text
        gen = Personal(locale)
        text = Text(locale)

        for _ in range(count):
            gen_post = Contact(
                name=gen.name(),
                num=gen.credit_card_number(),
                some_blank=text.text(3),
                some_null=gen.email()
            )
            gen_post.save()

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Parallel(models.Model):
    field1 = models.CharField(max_length=10)
    field2 = models.CharField(max_length=10)

    @staticmethod
    def init(count=2000, locale='en'):
        from elizabeth import Generic, Text
        text = Text(locale)

        for _ in range(count):
            gen_post = Parallel(
                field1=text.word(),
                field2=text.word(),
            )
            gen_post.save()


class Post(models.Model):
    author = models.ForeignKey(User)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return '{}: {}...'.format(self.author, self.text[:25])

    @staticmethod
    def init(count=2000, locale='en'):
        from elizabeth import Generic, Text
        from random import randint, choice
        gen = Generic(locale)
        text = Text(locale)

        for _ in range(count):
            gen_post = Post(
                author=choice(User.objects.all()),
                text=text.text(5),
                likes=randint(0, 100)
            )
            gen_post.save()

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    time = models.DateTimeField(auto_now=True)
    text = models.TextField()
    likes = models.PositiveSmallIntegerField(default=0)
    post = models.ForeignKey(Post)

    def __str__(self):
        return "{}: {}...".format(self.post.author, self.text[:50])

    @staticmethod
    def init(count=20000, locale='en'):
        from elizabeth import Text
        from random import randint, choice
        text = Text(locale)
        posts = list(Post.objects.all())

        for _ in range(count):
            gen_post = Comment(
                post=choice(posts),
                text=text.text(2),
                likes=randint(0, 100)
            )
            gen_post.save()

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
