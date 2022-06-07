
from django.urls import reverse_lazy
from .models import Blog
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    TemplateView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.


# def homepage(request):
#     blogs = Blog.objects.all()
#     content = {'title': 'Home Django',
#                'blogs': blogs
#                }
#     return render(request, 'blog_app/homepage.html', content)


class HomeListView(ListView):  # Class based view
    model = Blog
    context_object_name = 'blogs'
    extra_context = {'title': 'Home Django Project'}
    ordering = ["-post_created"]
    template_name = 'blog_app/homepage.html'
    paginate_by = 5


class PostDetailView(DetailView):
    model = Blog
    template_name = 'blog_app/blog_detail.html'
    context_object_name = 'blog'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['title', 'content']
    extra_context = {'button_name': 'create'}

    # overright the form
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    fields = ['title', 'content']
    template_name = 'blog_app/blog_form.html'
    extra_context = {'button_name': 'update',
                     'title': 'Update Post'}

    # overright the form
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog-homepage')
    template_name = 'blog_app/blog_confirm_delete.html'
    context_object_name: 'object'

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        else:
            return False


class AboutTemplateView(TemplateView):
    extra_context = {'title': 'About Django'}
    # with template view it is important to get give a template_name
    template_name = 'blog_app/about.html'

# def about(request):

#     return render(request, 'blog_app/about.html', {'title': 'About Django'})
