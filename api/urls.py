from django.urls import path
from .views import DetailKol, ListKol, RegisterView, ListMoin, DetailMoin, ListTafsili, DetailTafsili, ListSanad, DetailSanad, ListArtykl, DetailArtykl

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('Kol', ListKol.as_view(), name='kol'),
    path('Kol/<int:pk>', DetailKol.as_view(), name='singlekol'),
    path('Moin', ListMoin.as_view(), name='moin'),
    path('Moin/<int:pk>', DetailMoin.as_view(), name='singlemoin'),
    path('Tafsili', ListTafsili.as_view(), name='tafsili'),
    path('Tafsili/<int:pk>', DetailTafsili.as_view(), name='singletafsili'),
    path('Sanad', ListSanad.as_view(), name='sanad'),
    path('Sanad/<int:pk>', DetailSanad.as_view(), name='singlesanad'),
    path('Artykl', ListArtykl.as_view(), name='artykl'),
    path('Artykl/<int:pk>', DetailArtykl.as_view(), name='singleartykl'),
]
