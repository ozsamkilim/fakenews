from django.shortcuts import render
from .models import Article

from .forms import CommentForm

# Create your views here.


def index(request):
	articles = Article.objects.all()
	context={'articles':articles}
	return render(request, 'index.html', context)


def article(request,article_id):
	article = Article.objects.get(id=article_id)
	context={'article':article}
	return render(request, 'article.html', context)





def form(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = CommentForm()
    return render(request, 'article.html', {'form': form})

