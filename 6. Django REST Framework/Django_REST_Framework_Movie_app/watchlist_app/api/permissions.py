from rest_framework import permissions


class IsReviewerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # review user na like thakle only read korbe and reviewer user hole update delete korte parbe
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.reviewer == request.user
