from django.db import models
from django.db.models import JSONField


class Vendor(models.Model):
    name=models.CharField(max_length=100)
    contact_details=models.TextField()
    address=models.TextField()
    vendor_code=models.CharField(max_length=100,unique=True)
    on_time_delivery_rate=models.FloatField(null=True,default=0)
    quality_rating_avg=models.FloatField(null=True,default=0)
    average_resonse_time=models.FloatField(null=True,default=0)
    fulfillment_rate=models.FloatField(null=True,default=0)
    
    def __str__(self):
        return self.name
    
class PurchaseOrder(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )
    
    po_number=models.CharField(max_length=100,unique=True)
    vendor=models.ForeignKey(Vendor,related_name='purchase_order',on_delete=models.CASCADE)
    order_date=models.DateTimeField()
    delivery_date=models.DateTimeField()
    items=models.JSONField()
    quantity=models.IntegerField()
    status=models.CharField(max_length=10,choices=STATUS_CHOICES)
    quality_rating=models.FloatField(null=True,default=0)
    issue_date=models.DateTimeField()
    acknowledgment_date=models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return self.po_number

class HistoricalPerformance(models.Model):
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE)
    date=models.DateTimeField()
    on_time_delivery_rate=models.FloatField(null=True,default=0)
    quality_rating_avg=models.FloatField(null=True,default=0)
    average_response_time=models.FloatField(null=True,default=0)
    fullfillment_rate=models.FloatField(null=True,default=0)
    
    def __str__(self):
        return f"{self.vendor.name} - {self.date}"
        
