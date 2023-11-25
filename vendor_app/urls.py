from django.urls import path
from .views import ( VendorListCreateView, 
                    VendorRetrieveUpdateDeleteView ,
                    PurchaseOrderListCreateView, 
                    PurchaseOrderRetrieveUpdateDeleteView ,
                    HistoricalPerformanceDetailView
                    )
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('token/', obtain_auth_token, name='api_token_auth'),
    
    #############  Vendor  ###############################
    path('vendors/', VendorListCreateView.as_view(), name='vendor-list-create'),
    path('vendors/<int:pk>/', VendorRetrieveUpdateDeleteView.as_view(), name='vendor-retrieve-update-delete'),
    
    
    #############   Purchase Order Part ######################
    path('purchase_orders/', PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
    path('purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDeleteView.as_view(), name='purchase-order-retrieve-update-delete'),


    #############################  Performance history #####################
     path('vendors/<int:vendor>/historical_performance/', HistoricalPerformanceDetailView.as_view(), name='vendor-historical-performance-detail'),
]

