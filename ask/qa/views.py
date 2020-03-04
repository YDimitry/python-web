from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.decorators.http import require_GET

from qa.models import Question, Answer

@require_GET
def index(request, *args, **kwargs):
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1
    posts = Question.objects.new()
    paginator = Paginator(posts, 2)
    paginator.baseurl = '/?page='
    posts_page = paginator.get_page(page)
    page = paginator.page(page)
    return render(request, 'main.html', {'post_list': posts_page,
                                         'paginator': paginator, 'page': page, 'popular': False })

def login(request, *args, **kwargs):
    return HttpResponse('You re at the qa login')


def signup(request, *args, **kwargs):
    return HttpResponse('You re at the qa signup')


def question(request, *args, **kwargs):
    try:
        q_id = int(kwargs.get('id'))
    except ValueError:
        q_id = False
    if q_id:
        post = Question.objects.get(pk=q_id)
        answers = Answer.objects.all().filter(question=post)
        return render(request, 'question.html', {'post': post,'answers':answers})
    else:
        return HttpResponse(content='Такого вопроса несуществует',
                                content_type='text/html',
                                status=404)

def ask(request, *args, **kwargs):
    return HttpResponse('You re at the qa ask')

@require_GET
def popular(request, *args, **kwargs):
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1
    posts = Question.objects.popular()
    paginator = Paginator(posts, 2)
    paginator.baseurl = 'popular/?page='
    posts_page = paginator.get_page(page)
    page = paginator.page(page)
    return render(request, 'main.html', {'post_list': posts_page,
                                         'paginator': paginator, 'page': page, 'popular': 'Поулярные'})


def new(request, *args, **kwargs):
    return HttpResponse('You re at the qa new')

def makeQuestions():
    q = Question()
    q.title = 'posuere lorem ipsum'
    q.text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    Felis imperdiet proin fermentum leo vel orci porta non. Non quam lacus
    suspendisse faucibus interdum posuere lorem ipsum dolor. Pharetra magna
    ac placerat vestibulum lectus mauris ultrices. Bibendum neque egestas congue quisque."""

    q.author = User.objects.create_user(username='Dewey Jackson')
    q.save()

    q = Question()
    q.title = 'tristique nulla aliquet'
    q.text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    Sed risus ultricies tristique nulla aliquet enim tortor at auctor.
    Sed felis eget velit aliquet. Et molestie ac feugiat sed. Vitae semper
    quis lectus nulla at volutpat diam ut."""
    q.author = User.objects.create_user(username='Randall Brown')
    q.save()

    q = Question()
    q.title = 'pellentesque diam volutpat'
    q.text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
    dolore magna aliqua. Platea dictumst quisque sagittis purus sit. Ac feugiat sed lectus vestibulum mattis ullamcorper.
    Donec et odio pellentesque diam volutpat. Adipiscing elit ut aliquam purus sit amet. """
    q.author = User.objects.create_user(username='Lewis Clayton')
    q.save()

    q = Question()
    q.title = 'Eu lobortis elementum'
    q.text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
    dolore magna aliqua. Eu lobortis elementum nibh tellus molestie nunc non blandit. Sodales ut eu sem integer vitae
    justo eget magna fermentum. Nisi est sit amet facilisis. Phasellus egestas tellus rutrum tellus pellentesque eu
    tincidunt. """
    q.author = User.objects.create_user(username='Tiffany Schneider')
    q.save()

    q = Question()
    q.title = 'Neque gravida in fermentum'
    q.text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
    dolore magna aliqua. Neque gravida in fermentum et sollicitudin ac orci phasellus egestas. Viverra tellus in hac
    habitasse. Netus et malesuada fames ac turpis egestas. Dui vivamus arcu felis bibendum. """
    q.author = User.objects.create_user(username='Tasha Williams')
    q.save()
    return HttpResponse('data created')

def makeAnswers():
    post = Question.objects.get(pk=2)

    ans = Answer()
    ans.question = post
    ans.text = """Vitae nunc sed velit dignissim. Accumsan lacus vel facilisis volutpat est velit egestas dui id. Posuere
    urna nec tincidunt praesent. Ullamcorper eget nulla facilisi etiam dignissim diam quis enim lobortis. """
    ans.author = User.objects.get(username='Geraldine Carter')
    ans.save()

    ans = Answer()
    ans.question = post
    ans.text = """Hendrerit dolor magna eget est lorem ipsum dolor. Id faucibus nisl tincidunt eget nullam non nisi est
    sit. Lectus vestibulum mattis ullamcorper velit sed ullamcorper morbi. Nam at lectus urna duis convallis convallis
    tellus id. """
    ans.author = User.objects.get(username='Adrienne Lawrence')
    ans.save()

    ans = Answer()
    ans.question = post
    ans.text = """Proin fermentum leo vel orci porta non pulvinar. Ac odio tempor orci dapibus. Dictum at tempor commodo
    ullamcorper a lacus vestibulum sed arcu. In vitae turpis massa sed elementum. """
    ans.author = User.objects.get(username='Stewart Miller')
    ans.save()

    ans = Answer()
    ans.question = post
    ans.text = """Urna neque viverra justo nec ultrices dui sapien. Cursus metus aliquam eleifend mi in nulla. Tempor
    commodo ullamcorper a lacus vestibulum sed. Eget sit amet tellus cras adipiscing enim eu turpis egestas. """
    ans.author = User.objects.get(username='Joann Castro')
    ans.save()

    ans = Answer()
    ans.question = post
    ans.text = """Integer enim neque volutpat ac tincidunt. Quis varius quam quisque id diam vel quam elementum. Amet
    risus nullam eget felis eget nunc lobortis mattis aliquam. Dis parturient montes nascetur ridiculus mus. """
    ans.author = User.objects.get(username='Tricia Goodwin')
    ans.save()