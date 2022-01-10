from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from anestudy.models.blog import Article, Comment, Tag
from anestudy.forms import UserCreationForm, ProfileForm, CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.core.mail import send_mail
from django.core.paginator import Paginator
import os

def index(request):
    ranks = Article.objects.order_by('-count')[:2]
    objs = Article.objects.all()[:3]
    context = {
        'title': 'omh-site',
        'articles': objs,
        'ranks': ranks,
    }
    return render(request, 'anestudy/index.html', context)


class Login(LoginView):
    template_name = 'anestudy/auth.html'

    def form_valid(self, form):
        messages.success(self.request, 'ログイン完了')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'ログインエラー')
        return super().form_invalid(form)

def signup(request):
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            #user.is_active = False
            user.save()
            #ログインさせる
            login(request, user)
            messages.success(request, '登録完了')
            return redirect('/')
    return render(request, 'anestudy/auth.html', context)

from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class MypageView(LoginRequiredMixin, View):
    context = {}

    def get(self, request):
        return render(request, 'anestudy/mypage.html', self.context)

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, '更新完了')
        return render(request, 'anestudy/mypage.html', self.context)

def contact(request):
    context = {}
    if request.method == 'POST': 
        # --- email to me ---
        subject = 'お問い合わせがありました'
        message = """お問い合わせがありました。\n名前: {}\nメールアドレス: {}\n内容: {}""".format(
            request.POST.get('name'), 
            request.POST.get('email'), 
            request.POST.get('content'))
        
        email_from = os.environ['DEFAULT_EMAIL_FROM']
        email_to = [os.environ['DEFAULT_EMAIL_FROM'],]
        send_mail(subject,message,email_from,email_to,)
        # --- email to me ---
        messages.success(request, 'お問い合わせいただきありがとうございます')

    return render(request, 'anestudy/contact.html', context)

def blogs(request):
    objs = Article.objects.all()
    paginator = Paginator(objs, 2)
    page_number = request.GET.get('page')
    context = {
        'page_title': '記事一覧',
        'page_obj': paginator.get_page(page_number),
        'page_number': page_number,
    }
    return render(request, 'anestudy/blogs.html', context)

def article(request, pk):
    obj = Article.objects.get(pk=pk)
    if request.method == 'POST':
        if request.POST.get('like_count', None):
            obj.count += 1
            obj.save()
        else:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.article = obj
                comment.save()
    comments =  Comment.objects.filter(article=obj)
    context = {
        'article': obj,
        'comments': comments,
    }
    return render(request, 'anestudy/article.html', context)

def tags(request, slug):
    tag = Tag.objects.get(slug=slug)
    objs = tag.article_set.all()

    paginator = Paginator(objs, 2)
    page_number = request.GET.get('page')
    context = {
        'page_title': tag.name,
        'page_obj': paginator.get_page(page_number),
        'page_number': page_number,
    }
    return render(request, 'anestudy/blogs.html', context)
