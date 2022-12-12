from django.shortcuts import render
from .models import Article
from .forms import ArticleForm
from django.utils import timezone
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User
from .utils import sendTransiction
import json
import hashlib

def home(request):
    context = {
        'article' : Article.objects.all()
    }
    return render(request, 'homepage.html', context)

def post_new(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()


            jsonObj = {}
            jsonObj["title"] = post.title
            jsonObj["description"] = post.text
            message = json.dumps(jsonObj)
            # message2 = post.title + post.text
            # message1 = message.encode('utf-8')
            hashed_message = hashlib.sha256(message.encode('utf-8')).hexdigest()
            # print(message2)
            # print(message1)
            # print(message)
            print(hashed_message)
            sendTransiction(hashed_message)

            return HttpResponseRedirect("/")
    else:
        post = ArticleForm()
    context = {
        'form' : ArticleForm()
    }
    return render(request, 'post_edit.html', context)


def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        'user' : user
    }
    return render(request, 'profile.html', context)

def search(request):
    if 'q' in request.GET:
        querystring = request.GET.get('q')
        if len(querystring) == 0:
            return HttpResponseRedirect("/search/")
        article = Article.objects.filter(transaction_id__icontains=querystring)
        context = {
            'article' : article
        }
        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html')
