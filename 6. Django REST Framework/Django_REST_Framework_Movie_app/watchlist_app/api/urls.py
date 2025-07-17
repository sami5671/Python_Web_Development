from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("movies", views.MovieListViewSet, basename="movielist")
router.register("reviews", views.ReviewListViewSet, basename="review")

urlpatterns = [
    # path("", views.movie_list),
    # path("<pk>/", views.movie_detail)
    # path("", views.MovieListCreateView.as_view()),
    # path("<pk>/", views.MovieDetailView.as_view()),
    # path("reviews/", views.ReviewListCreateView.as_view(), name="review_list"),
    # path("reviews/<pk>/", views.ReviewDetailView.as_view(), name="review_detail"),
    # -----------Model viewSet routing ------------
    path("", include(router.urls))
]
