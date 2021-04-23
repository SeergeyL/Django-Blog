from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from posts.forms import PostForm, CommentForm
from posts.models import Post, PostCategory, User, Follow, Comment


def index(request):
    """
    Renders main page with all users posts and category navigation
    """
    posts = Post.objects.order_by('-pub_date')
    categories = PostCategory.objects.all()

    return render(request, "index.html", {"posts": posts, "categories": categories})


def category_page(request, slug):
    """
    Renders category specific posts and category navigation
    """
    posts = Post.objects.filter(category__slug=slug).order_by('-pub_date')
    categories = PostCategory.objects.all()

    return render(request, "index.html", {"posts": posts, "categories": categories})


def post_page(request, post_id):
    """
    Renders Post page and form to add comments
    """
    post = Post.objects.get(pk=post_id)
    form = CommentForm()

    return render(request, "post.html", {"post": post, 'form': form})


def profile(request, username):
    """
    Renders profile page with user posts
    """
    user = get_object_or_404(User, username=username)
    user_posts = user.posts.all()
    follow_status = user.following.filter(blogger__username=username).exists()

    return render(request, 'profile.html', {'posts': user_posts, "author": user, "following": follow_status})


@login_required
def new_post(request):
    """
    Renders form to create new post
    """
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()
            return redirect('post', post_id=post.pk)

    return render(request, 'new_post.html', {"form": form})


@login_required
def edit_post(request, post_id):
    """
    Renders form to edit post with specified post_id.
    Only author of the post can edit the form otherwise user will be redirected to post page
    """

    post = get_object_or_404(Post, pk=post_id)

    if request.user != post.author:
        return redirect('index')

    form = PostForm(request.POST or None, files=request.FILES or None, instance=post)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('post', post_id=post.pk)

    return render(request, 'new_post.html', {"form": form, "post": post})


@login_required
def delete_post(request, post_id):
    """
    Deletes the post with specified post_id and redirect to main page.
    Only author can delete the post.
    """

    post = get_object_or_404(Post, pk=post_id)

    if post.author != request.user:
        return redirect('index')

    post.delete()

    return redirect('index')


@login_required
def add_comment(request, post_id):
    """
    Add comment to post with specified post_id and redirect to post page with post_id
    """
    post = get_object_or_404(Post, pk=post_id)

    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            form.save()
            return redirect('post', post_id=post_id)


@login_required
def delete_comment(request, post_id, comment_id):
    """
    Deletes comment under the post. The comment can be deletted only by author of the post
    or comment author
    """

    post = get_object_or_404(Post, pk=post_id)
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user == post.author or request.user == comment.author:
        comment.delete()
        return redirect('post', post_id=post_id)

    return redirect('post', post_id=post_id)


@login_required
def follow(request, username):
    """
    Follow the user with specified username if not followed yet.
    Doesn't allow to follow yourself
    """

    follow_status = request.user.follower.filter(blogger__username=username).exists()

    if not follow_status and username != request.user.username:
        author = get_object_or_404(User, username=username)
        Follow.objects.create(user=request.user, blogger=author)

    return redirect('profile', username=username)


@login_required
def unfollow(request, username):
    """
    Unfollow the user with specified username
    """
    request.user.follower.filter(blogger__username=username).delete()

    return redirect('profile', username=username)

