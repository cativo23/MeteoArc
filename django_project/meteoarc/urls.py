from django.conf.urls import url
from .views import ListSongsView, SongDetail, SongsList, SongPost, ListDatoView, DatoDetail, DatoList, DatoPost, Index


urlpatterns = [
    url(r'', Index.as_view(), name="songs-all"),
    url(r'songs/', ListSongsView.as_view(), name="songs-all"),
    url(r'songs2/', SongsList.as_view()),
    url(r'songs3/(?P<pk>\d+)/', SongDetail.as_view()),
    url(r'create-survey/$', SongPost.as_view(), name ='create-survey') ,
    url(r'datos/', ListDatoView.as_view(), name="songs-all"),
    url(r'datos2/', DatoList.as_view()),
    url(r'datoss/(?P<pk>\d+)/', DatoDetail.as_view()),
    url(r'crear-dato/$', DatoPost.as_view(), name ='create-survey') ,
]
