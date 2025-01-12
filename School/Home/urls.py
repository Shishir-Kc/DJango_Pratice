from django.urls import path
from Home import views
from django.views.generic import TemplateView 

app_name ="Home"

urlpatterns = [ 
    path('',views.Notice.as_view(),name='home'),  
    path('notice/',views.Notice.as_view(),name='notice'),
    path('notice/<int:pk>',views.NoticeDetail.as_view(),name='notice_detail'),
    path('notice/delete/<int:pk>',views.NoticeDelete.as_view(),name='notice_delete'),
    path('notice/add/',views.NoticeAdd.as_view(),name='notice_add'),
]