import random
from django.core.paginator import Paginator
from posts.models import Post


def get_random_posts(n=5):
    """ Return n random posts from database """

    valid_post_ids = list(Post.objects.values_list('pk', flat=True))
    random_post_ids = random.sample(valid_post_ids, min(len(valid_post_ids), n) )
    random_posts = Post.objects.filter(pk__in=random_post_ids)
    return random_posts


def setup_paginator(items, request, items_per_page=10):
    """ Setup paginator and returns page and paginator """

    paginator = Paginator(items, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return page, paginator