from django.conf.urls import url
from .views import ListSongsView, SongDetail, SongsList, SongPost


urlpatterns = [
    url(r'songs/', ListSongsView.as_view(), name="songs-all"),
    url(r'songs2/', SongsList.as_view()),
    url(r'songs3/(?P<pk>\d+)/', SongDetail.as_view()),
    url(r'create-survey/$', SongPost.as_view(), name ='create-survey') ,

]
