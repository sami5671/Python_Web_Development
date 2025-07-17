import django_filters.rest_framework
from django.shortcuts import get_object_or_404
from rest_framework import generics, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from watchlist_app import models

from . import permissions, serializers

# ----------Function based views--------------

# @api_view()
# def movie_list(request):
#     movies = models.MovieList.objects.all()  # python objects
#     serializer = serializers.MovieListSerializer(
#         movies, many=True
#     )  # python object ot json convert
#     return Response(serializer.data)


# @api_view(["GET", "POST"])
# def movie_list(request):
#     if request.method == "GET":
#         movies = models.MovieList.objects.all()  # python objects
#         serializer = serializers.MovieListSerializer(
#             movies, many=True
#         )  # python object ot json convert
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = serializers.MovieListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


# @api_view(["GET", "PUT", "PATCH", "DELETE"])
# # PUT---> take whole object
# def movie_detail(request, pk):
#     movie = get_object_or_404(models.MovieList, pk=pk)

#     if request.method == "GET":
#         serializer = serializers.MovieListSerializer(movie)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == "PUT":
#         serializer = serializers.MovieListSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == "PATCH":
#         serializer = serializers.MovieListSerializer(
#             movie, data=request.data, partial=True
#         )
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == "DELETE":
#         movie.delete()
#         return Response({"message": "Movie deleted Successfully"})


# ----------Class based views--------------
# 1. list of all movies, create a new movie
# class MovieListCreateView(generics.ListCreateAPIView):
#     queryset = models.MovieList.objects.all()
#     serializer_class = serializers.MovieListSerializer


# # single movie/update/delete
# class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.MovieList.objects.all()
#     serializer_class = serializers.MovieListSerializer


# class ReviewListCreateView(generics.ListCreateAPIView):
#     queryset = models.Reviews.objects.all()
#     serializer_class = serializers.ReviewSerializer


# # single movie/update/delete
# class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Reviews.objects.all()
#     serializer_class = serializers.ReviewSerializer


# ----------Model viewSet --------------
class MovieListViewSet(viewsets.ModelViewSet):
    queryset = models.MovieList.objects.prefetch_related(
        "reviews"
    )  # m2m , reverse foreign key relation
    serializer_class = serializers.MovieListSerializer


class ReviewListViewSet(viewsets.ModelViewSet):
    queryset = models.Reviews.objects.select_related("movie")
    serializer_class = serializers.ReviewSerializer
    # permission_classes = [permissions.IsReviewerOrReadOnly, IsAuthenticated]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # filterset_fields = ["reviewer", "rating"]
    filterset_fields = ["reviewer__username", "rating"]
