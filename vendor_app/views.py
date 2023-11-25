from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Vendor , PurchaseOrder , HistoricalPerformance
from .serializers import VendorSerializer , PurchaseOrderSerializer,HistoricalPerformanceSerializer



#############  Vendor  ###############################

class VendorListCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [permissions.IsAuthenticated]


class VendorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [permissions.IsAuthenticated]


#############   Purchase Order Part ######################

class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class PurchaseOrderRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer



#############  Vendor Performance ######################

class HistoricalPerformanceDetailView(generics.RetrieveAPIView):
    serializer_class = HistoricalPerformanceSerializer
    lookup_field = 'vendor'  

    def get_queryset(self):
        vendor_id = self.kwargs['vendor']
        return HistoricalPerformance.objects.filter(vendor=vendor_id)