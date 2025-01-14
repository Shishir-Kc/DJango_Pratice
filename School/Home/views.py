from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from django.views.generic import TemplateView , ListView ,CreateView, DetailView ,DeleteView
from django.urls import reverse_lazy
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



def Home(request):
    
    # if "search" in request.session:
    #     search_keyword = request.session['search']
    #     notice = models.Notice.objects.filter(Topic__icontains=search_keyword)
    #     context =  {
    #         'Notices':notice,
    #         'user':request.user
    #     }
    
    notice = models.Notice.objects.filter(user=request.user)
    context =  {
        'Notices':notice,
        'user':request.user
    }
    return render(request,'Home/home.html',context)

class NoticeDetail(DetailView):
    template_name = 'Home/noticeDetail.html'
    context_object_name = 'Notice'
    model = models.Notice






@login_required
def NoticeAdd(request):
    if request.method == "POST":
        data_topic = request.POST.get("topic_name")
        data_news = request.POST.get("news")
        data = models.Notice(user=request.user,Topic=data_topic,News=data_news)
        data.save()
        return redirect('Home:home')
    
    else:
        return render(request,'Home/notice_form.html')





def USER_LOGIN(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        user_pass = request.POST.get("user_pass")
        user = authenticate(request,username=user_name,password=user_pass)
        if user is not None:
            login(request,user)
            return redirect('Home:home')
        
    else:
        return render(request,'Home/login.html')
    
@login_required
def AddUser(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        user_pass = request.POST.get("user_pass")
        user = User.objects.create_user(username=user_name,password=user_pass)
        user.save()
        return redirect('Home:login')
    else:
        return render(request,'Home/base.html')
    

@login_required
def user_logout(request):
    logout(request)
    return redirect('Home:login')

@login_required
def update_notice(request,notice_id):
    if request.method == "POST":
        id = request.POST.get('notice_id')
        updated_topic = request.POST.get('topic_name')
        updated_news = request.POST.get('news')
        data = models.Notice.objects.get(id=id)
        data.Topic = updated_topic
        data.News = updated_news
        data.save()
        return redirect('Home:home')

    else:
        data = models.Notice.objects.get(id=notice_id)
        context = {
            'Notice':data
        }
        return render(request,'Home/update.html',context)
    
@login_required
def notice_detail(request,notice_id):
    if request.method =="POST":
        pass
    else:
        data = models.Notice.objects.get(id=notice_id)
        context = {
            'Notice':data
        }
        return render(request,'Home/detail.html',context)

@login_required
def delete_notice(request,notice_id):
    data = models.Notice.objects.get(id=notice_id)
    data.delete()
    return redirect('Home:home')


@login_required
def search(request):
    request.session['search'] = request.GET.get('search')
    return redirect('Home:home')