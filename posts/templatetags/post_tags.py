import random
from django import template
from posts.models import Post


register = template.Library()


@register.inclusion_tag('random_posts.html')
def generate_random_posts(n=5):
    valid_post_ids = list(Post.objects.values_list('pk', flat=True))
    random_post_ids = random.sample(valid_post_ids, min(len(valid_post_ids), n) )
    random_posts = Post.objects.filter(pk__in=random_post_ids)

    return {"random_posts": random_posts}
