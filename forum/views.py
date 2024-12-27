from django.shortcuts import render, redirect
from .mixins import UserIsOwnerMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from forum import models
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .forms import ForumFormCreate, ForumFormEdit, CommentForm


# Create your views here.

class ForumListView(ListView):
    model = models.Forum
    context_object_name = "forums"
    template_name = 'forum/forum_list.html'


class ForumCreateView(CreateView):
    model = models.Forum
    template_name = 'forum/forum_create.html'
    form_class = ForumFormCreate
    success_url = reverse_lazy('forum-list')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class ForumDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = models.Forum
    template_name = 'forum/forum_delete.html'
    success_url = reverse_lazy('forum-list')


class ForumEditView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = models.Forum
    template_name = 'forum/forum_edit.html'
    form_class = ForumFormEdit
    success_url = reverse_lazy('forum-list')


class ForumDetailView(DetailView):
    model = models.Forum
    context_object_name = "forum"
    template_name = 'forum/forum_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()  # Додаємо порожню форму коментаря в контекст
        return context

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.forum = self.get_object()
            comment.save()
            return redirect('forum-detail', pk=comment.forum.pk)
        else:
            # Тут можна обробити випадок з невалідною формою
            pass