from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Vendor,PurchaseOrder,HistoricalPerformance
from .serializers import VendorSerializer,PurchaseOrderSerializer,HistoricalPerformanceSerializer
from django.utils import timezone
from django.db.models import Avg,Count,F


class VendorListCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    Permission_classes=[IsAuthenticated]
    
class VendorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    Permission_classes=[IsAuthenticated]
    

class VendorPerformanceView(APIView):
    def get(self,request,pk):
        try:
            vendor=Vendor.objects.get(pk=pk)
        except Vendor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
        performance_date={
            'on_time_delivery_rate':vendor.on_time_delivery_rate,
            'quality_rating_avg':vendor.quality_rating_avg,
            'average_response_time':vendor.average_resonse_time,
            'fulfillment_rate':vendor.fulfillment_rate
        }
        return Response(performance_date)
    

class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    

class PurchaseOrderAcknowledgeView(APIView):
    def post(self,request,pk):
        try:
            purchase_order=PurchaseOrder.objects.get(pk=pk)
        except PurchaseOrder.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        purchase_order.acknowledgment_date=timezone.now()
        purchase_order.status="Completed"
        purchase_order.save()
        
        return Response(status=status.HTTP_200_OK) 
    

class HistoricalPerformanceListView(generics.ListAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer
    


class HistoricalPerformanceDetailView(generics.RetrieveAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer
    
    def get_queryset(self):
        vendor_code=self.kwargs.get('vendor_code',None)
        queryset =self.queryset.filter(vendor_id=vendor_code)
        return queryset
           