from django.urls import path
from Home import views

app_name ="Home"

urlpatterns = [ 
    path('',views.home,name="Home"),

]