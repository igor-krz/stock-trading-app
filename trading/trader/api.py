from .models import CustomUser, Stocks
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, StockSerializer
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
# Lead Viewset
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    def get_queryset(self):
        """
        This view should return data
        for the currently authenticated user.
        """
        user = self.request.user
        return CustomUser.objects.filter(username=user)

class StockViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = StockSerializer
    def get_queryset(self):
        """
        Optionally restricts the returned stocks to a given user,
        by filtering against a `userID` query parameter in the URL.
        """
        queryset = Stocks.objects.all()
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(userID=user)
        return queryset