from api.models import Kol, Moin, Sanad, Artykl, Tafsili
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from .serializers import KolSerializer, MoinSerializer, UserSerializer, TafsiliSerializer, SanadSerializer, ArtyklSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListKol(generics.ListCreateAPIView):
    queryset = Kol.objects.all()
    serializer_class = KolSerializer


class DetailKol(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kol.objects.all()
    serializer_class = KolSerializer


class ListMoin(generics.ListCreateAPIView):
    queryset = Moin.objects.all()
    serializer_class = MoinSerializer


class DetailMoin(generics.RetrieveUpdateDestroyAPIView):
    queryset = Moin.objects.all()
    serializer_class = MoinSerializer


class ListTafsili(generics.ListCreateAPIView):
    queryset = Tafsili.objects.all()
    serializer_class = TafsiliSerializer


class DetailTafsili(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tafsili.objects.all()
    serializer_class = TafsiliSerializer


class ListSanad(generics.ListCreateAPIView):
    # queryset = Sanad.objects.raw("""
    #                             SELECT a.id, a.date, a.note, a.date_created, sum(b.bed) bed, sum(b.bes) bes
    #                             FROM api_sanad a inner join api_artykl b on a.id = b.sanad_id
    #                             group by a.id, a.date, a.note, a.date_created;""")
    queryset = Sanad.objects.all()
    serializer_class = SanadSerializer


class DetailSanad(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sanad.objects.all()
    serializer_class = SanadSerializer


class ListArtykl(generics.ListCreateAPIView):
    queryset = Artykl.objects.all()
    serializer_class = ArtyklSerializer


class DetailArtykl(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artykl.objects.all()
    serializer_class = ArtyklSerializer
