from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.views.generic import TemplateView , ListView ,CreateView, DetailView ,DeleteView
from django.urls import reverse_lazy

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