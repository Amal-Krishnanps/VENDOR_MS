from django.db.models.signals import post_save,pre_delete
from django.dispatch import receiver
from .models import Vendor,PurchaseOrder,HistoricalPerformance
from django.db.models import F,Avg,Count
from django.utils import timezone

@receiver(post_save, sender=PurchaseOrder)
@receiver(pre_delete, sender=PurchaseOrder)
def update_vendor_performance(sender,instance,**kwargs):
    vendor=instance.vendor
    
    #completed purchase orders
    completed_orders=PurchaseOrder.objects.filter(vendor=vendor,status='Completed')
    completed_orders_no=completed_orders.count()
    
    
    
    #calculate on time delivery rate
    def calculate_on_time_delivery_rate():
        if completed_orders.exists():
            on_time_delivery_orders=completed_orders.filter(delivery_date__lte=instance.delivery_date).count()
            on_time_delivery_rate=(on_time_delivery_orders/completed_orders_no)*100
            return on_time_delivery_rate
        return 0
    
    #calculate quality rating average
    def calculate_quality_rating_average():
        if completed_orders.exists():
            quality_ratings = completed_orders.filter(quality_rating__isnull=False).values_list('quality_rating', flat=True)
            return sum(quality_ratings) / len(quality_ratings) if quality_ratings else 0
        return 0
    
    # average response time
    def calculate_average_response_time():
        acknowledged_orders=completed_orders.filter(acknowledgment_date__isnull=False)
        if acknowledged_orders.exists():
            response_times = acknowledged_orders.aggregate(avg_response_time=Avg(F('acknowledgment_date') - F('issue_date')))['avg_response_time']
            avg_rt= response_times.total_seconds() / acknowledged_orders.count()
            return avg_rt
        return 0       
    
    # fullfillment rate
    def calculate_fullfillment_rate():
        if completed_orders.exists():
            total_orders=PurchaseOrder.objects.filter(vendor=vendor).count()
            return (completed_orders_no/total_orders)*100
        
    ## update vendor performance
    vendor.quality_rating_avg=calculate_quality_rating_average()
    vendor.on_time_delivery_rate=calculate_on_time_delivery_rate()
    vendor.average_resonse_time=calculate_average_response_time()
    vendor.fulfillment_rate=calculate_fullfillment_rate()
    
    vendor.save()
    
    
        # Save historical performance record if a change has been made
    #if kwargs.get('created') or kwargs.get('update_fields') or kwargs.get('deleted'):
    HistoricalPerformance.objects.create(
        vendor=vendor,
        date=timezone.now(),
        on_time_delivery_rate=vendor.on_time_delivery_rate,
        quality_rating_avg=vendor.quality_rating_avg,
        average_response_time=vendor.average_resonse_time,
        fullfillment_rate=vendor.fulfillment_rate
    )
                