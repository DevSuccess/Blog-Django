from . import views
from django.urls import path

app_name = 'posts'
urlpatterns = [
    path('', views.ArticleList.as_view(), name='home'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='detail')
]
