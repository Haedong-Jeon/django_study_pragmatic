from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy

from .models import Comment
from .forms import CommentCreationForm
from articleapp.models import Article

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        temp_comment = form.save(commit=False)
        temp_comment.article = Article.objects.get(pk=self.requset.POST['article_pk'])
        temp_comment.writer = self.request.user
        temp_comment.save()
        
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk':self.object.article.pk})
        return super().get_success_url()
