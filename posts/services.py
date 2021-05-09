import random
from posts.models import Post


def get_random_posts(n=5):
    """ Return n random posts from database """

    valid_post_ids = list(Post.objects.values_list('pk', flat=True))
    random_post_ids = random.sample(valid_post_ids, min(len(valid_post_ids), n) )
    random_posts = Post.objects.filter(pk__in=random_post_ids)
    return random_posts
