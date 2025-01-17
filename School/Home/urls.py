from django.urls import path
from Home import views
from django.views.generic import TemplateView 

app_name ="Home"

urlpatterns = [ 

    path('notice/',views.Home,name='home'),
   # path('notice/<int:pk>',views.NoticeDetail.as_view(),name='notice_detail'),
    # path('notice/delete/<int:pk>',views.NoticeDelete.as_view(),name='notice_delete'),
    path('notice/add/',views.NoticeAdd,name='notice_add'),
    path('accounts/login/',views.USER_LOGIN,name='login'),
    path('test/',views.AddUser,name='test'),
    path("logout/",views.user_logout,name='logout'),
    path('notice/update/<int:notice_id>',views.update_notice,name='update_notice'),
    path('notice/detail/<int:notice_id>',views.notice_detail,name='notice_detail'),
    path('notice/delete/<int:notice_id>',views.delete_notice,name='delete_notice'),
    path('search/',views.search,name='search'),
]