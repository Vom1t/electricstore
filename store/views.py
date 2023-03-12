from rest_framework.viewsets import ModelViewSet

from store.filter import RetailCountryFilter
from store.models import Retail
from store.serializers import RetailCreateSerializer, RetailUpdateSerializer, RetailSerializer


class RetailViewSet(ModelViewSet):
    queryset = Retail.objects.all()
    filterset_class = RetailCountryFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return RetailCreateSerializer
        elif self.action == 'update':
            return RetailUpdateSerializer
        else:
            return RetailSerializer