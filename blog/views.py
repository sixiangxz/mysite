from django.shortcuts import render
from django.http import HttpResponse
from .models import Entry,Author
from django.shortcuts import redirect
from . forms import NameForm, ContactForm, EntryForm
# Create your views here.
def index(request):

    # entry = Entry.objects.get(id=1)
    # author = Author.objects.filter(id=1).last()
    lis = [1, 2, 3, 4, 5]
    return  render(request, 'blog/index.html', locals())

def page(request,num=1):

    # for item in request.META:
    #     print(item,':', request.META.get(item))
    print(request.session)
    print(request.user)
    return render(request,'blog/blog_page.html')


def detail(request,num=1):

    return HttpResponse(num)





def get_name(request):

    if request.method == 'POST':

        form = NameForm(request.POST)

        if form.is_valid():
            print(type(form.cleaned_data))
            name = form.cleaned_data.get('username')
            print(name)
            pass
            return redirect('/blog/')
        else:
            render(request, 'blog/name.html', locals())

    else:
        form = NameForm()
    return render(request, 'blog/name.html', locals())

def contact(request):

    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            sender = form.cleaned_data.get('sender')
            cc_myself = form.cleaned_data.get('cc_myself')
            print(subject)
            print(message)
            print(sender)
            print(cc_myself)
            pass
            return redirect('/blog/')
        else:
            render(request, 'blog/contact.html', locals())

    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', locals())


def entry(request):

    if request.method == 'POST':

        form = EntryForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)

            form.save()
            return redirect('/blog/')
        else:
            render(request, 'blog/entry.html', locals())

    else:
        form = EntryForm()
    return render(request, 'blog/entry.html', locals())

from django.dispatch import Signal
from django.dispatch import receiver
from django.contrib import messages
# 自定义一个信号
work_done = Signal(providing_args=['path', 'time'])
# 发送器
def create_signal(request):

    messages.set_level(request, messages.WARNING)
    messages.add_message(request, messages.INFO, '提示信息')
    messages.warning(request, '警告信息！', extra_tags='hello')
    url_path = request.path
    print('我已经完成了工作，现在我正在发送一个信号出去给那些指定的接收器')
    work_done.send(create_signal, path=url_path, time='2016-06-06')
    return render(request, 'blog/mess.html', locals())

# 接收器
@receiver(work_done, sender=create_signal)
def my_callback(sender, **kwargs):
    print('我在%s时间，接收到了来自%s的信号，请求的url为%s' % (kwargs['time'], sender, kwargs['path']))

from django.core.paginator import PageNotAnInteger, Paginator,EmptyPage
# get_queryset().order_by('id')
def listing(request):
    entry_list = Entry.objects.get_queryset().order_by('id')
    print(Entry.objects.get_queryset())
    paginator = Paginator(entry_list, 2)
    page = request.GET.get('page')
    try:
        entries = paginator.page(page)
    except PageNotAnInteger:
        entries = paginator.page(1)
    except EmptyPage:
        entries = paginator.page(paginator.num_pages)
    return render(request, 'blog/list.html', locals())
