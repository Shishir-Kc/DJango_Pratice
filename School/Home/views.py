from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.views.generic import TemplateView , ListView ,CreateView, DetailView ,DeleteView
from django.urls import reverse_lazy
from . import forms

class Notice(ListView):
    model = models.Notice
    template_name = 'Home/home.html'
    context_object_name = 'Notices'

class NoticeDetail(DetailView):
    template_name = 'Home/noticeDetail.html'
    context_object_name = 'Notice'
    model = models.Notice




class NoticeDelete(DeleteView):
    model = models.Notice
    context_object_name = 'Notice'
    template_name = 'Home/notice_confirm_delete.html'
    success_url = reverse_lazy('Home:notice')


class NoticeAdd(CreateView):
    model = models.Notice
    template_name = 'Home/notice_form.html'
    fields = ['Topic','News','image']
    success_url = reverse_lazy('Home:notice')

def USER_LOGIN(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        user_pass = request.POST.get("user_pass")
        if user_name == 'admin' and user_pass == 'admin':
            return HttpResponse("Login Success")
        else:
            return HttpResponse("Login Failed")
    else:
        return render(request,'Home/login.html') 
    
    
def AddUser(request):
    if request.method == 'POST':
        form =  forms.StudentFrom(request.POST)
        if form.is_valid():
            print('Form is valid')
            data = form.cleaned_data
            print(request.POST.get("user_name"))
            print(request.POST.get("user_pass"))
            return HttpResponse("valid")
        
        else:
            print('Form is not valid')
            return HttpResponse("valid")

    else:
        context = {
                "form":forms.StudentFrom()
            }


        return render(request,'Home/test.html',context)