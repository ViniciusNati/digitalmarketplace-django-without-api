from django.urls import path
from .views import *
from . import views



urlpatterns = [
    path('', index.as_view(), name='index'),
    path('anunciar', AnunciarView),
    path('verified', VerifiedView),
    path('account', AccountView),
    path('profile/<str:username>/<int:id>', ProfileSlug, name='profile'),
    path('post/<slug:slug>/', PostView), #um path pra duas views, post e commentview
    #path('comments', CommentView),
   # path('template1', template1),
   # path('template2', template2),
   # path('template3', template3),
   # path('template4', template4),


 #   path('anuncio' , AnnounceView),

]
