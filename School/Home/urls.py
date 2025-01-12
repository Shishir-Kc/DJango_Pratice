from django.urls import path
from Home import views
from django.views.generic import TemplateView 

app_name ="Home"

urlpatterns = [ 
    path('',views.Notice.as_view(),name='home'),  

]