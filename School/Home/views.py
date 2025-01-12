from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.views.generic import TemplateView , ListView , DetailView ,DeleteView


class Notice(ListView):
    model = models.Notice
    template_name = 'Home/home.html'
    context_object_name = 'Notices'

class NoticeDetail(DetailView):
    pass