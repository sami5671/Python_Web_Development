from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import AuthorViewSet, BookViewSet, ContactViewSet, TaskViewSet

router = DefaultRouter()
router.register("tasks", TaskViewSet)
router.register("contacts", ContactViewSet)
router.register("authors", AuthorViewSet)
router.register("books", BookViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("login/", TokenObtainPairView.as_view(), name="login"),
]
