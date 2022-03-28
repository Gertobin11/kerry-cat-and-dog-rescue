from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm, PostForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'
    paginate_by = 6


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        template = "blog-detail.html"
        context = {
            'post': post,
            'comments': comments,
            'liked': liked,
            'commented': False,
            'comment_form': CommentForm()
        }

        return render(request, template, context)


    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        template = "blog-detail.html"
        context = {
            'post': post,
            'comments': comments,
            'liked': liked,
            'commented': True,
            'comment_form': CommentForm()
        }

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Your comment has been uploaded successfully')
        else:
            comment_form = CommentForm()
            messages.error(request, 'Sorry there was a problem with your comment upload, please try again')

        return render(request, template, context)


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user.id)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('blog_details', args=[slug]))


class PostFormView(generic.edit.FormView):
    form_class = PostForm
    success_url = '/blog/'
    template_name = 'blog-form.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


#class PostFormEdit(generic.edit.UpdateView):
