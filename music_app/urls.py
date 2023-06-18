from django.urls import path
from . import views

urlpatterns=[
    path('',views.homepage,name="HomePage"),
    path('about/',views.aboutpage,name="AboutPage"),
    path('upload/',views.uploadMusic,name="UploadMusic"),
]