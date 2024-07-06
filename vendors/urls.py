from django.urls import path
from vendors.views import (
    VendorListCreateView,VendorRetrieveUpdateDestroyView,VendorPerformanceView,
    PurchaseOrderListCreateView,PurchaseOrderRetrieveUpdateDestroyView,
    PurchaseOrderAcknowledgeView,HistoricalPerformanceListView,HistoricalPerformanceDetailView)

urlpatterns = [
    #Vendor
    path('api/vendors/',VendorListCreateView.as_view(), name='vendor_list_create'),
    path('api/vendors/<int:pk>/',VendorRetrieveUpdateDestroyView.as_view(), name='vendor_detail'),
    path('api/vendors/<int:pk>/performance/',VendorPerformanceView.as_view(), name='vendor_performance'),

    
    #Purchase Order
    path('api/purchase_orders/',PurchaseOrderListCreateView.as_view(), name='purchase_order_list_create'),
    path('api/purchase_orders/<int:pk>/',PurchaseOrderRetrieveUpdateDestroyView.as_view(),name='    '),
    path('api/purchase_orders/<int:pk>/acknowledge/',PurchaseOrderAcknowledgeView.as_view(),name='purchase_order_acknowledge'),
    
    #Historical Perfromance
    path('api/historical_performance/',HistoricalPerformanceListView.as_view(),name='historical_performance'),
    path('api/historical_performance/<int:pk>/',HistoricalPerformanceDetailView.as_view(),name='historical_performance_detail'),
    
    
    
    
]
