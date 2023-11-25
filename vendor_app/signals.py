# signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import  Count , Func, Avg, DurationField
from .models import PurchaseOrder, HistoricalPerformance, Vendor
from django.utils import timezone

# On-Time Delivery Rate
@receiver(post_save, sender=PurchaseOrder)
@receiver(post_delete, sender=PurchaseOrder)
def update_on_time_delivery_rate(sender, instance, **kwargs):
    if instance.status == "completed" or (hasattr(instance, '_state') and instance._state.adding):
        completed_orders = PurchaseOrder.objects.filter(vendor=instance.vendor, status="completed")
        on_time_delivered_orders = completed_orders.filter(delivery_date__lte=instance.delivery_date)

        total_completed = completed_orders.count()
        on_time_delivered = on_time_delivered_orders.count()

        on_time_delivery_rate = (on_time_delivered / total_completed) * 100 if total_completed > 0 else 0

        # Update or create HistoricalPerformance record
        historical_performance, created = HistoricalPerformance.objects.get_or_create(
            vendor=instance.vendor,
            date=instance.delivery_date.date(),
            defaults={
                'on_time_delivery_rate': on_time_delivery_rate,
                'quality_rating_avg': instance.vendor.quality_rating_avg,
                'average_response_time': instance.vendor.average_response_time,
                'fulfillment_rate': instance.vendor.fulfillment_rate,
            }
        )

        if not created:
            # Update existing HistoricalPerformance record
            historical_performance.on_time_delivery_rate = on_time_delivery_rate
            historical_performance.save()

        


# Quality Rating Average
@receiver(post_save, sender=PurchaseOrder)
def update_quality_rating_avg(sender, instance, **kwargs):
    if instance.status == "completed" and instance.quality_rating is not None:
        completed_orders = PurchaseOrder.objects.filter(vendor=instance.vendor, status="completed")
        quality_rating_avg = completed_orders.aggregate(Avg('quality_rating'))['quality_rating__avg']

        # Update or create HistoricalPerformance record
        historical_performance, created = HistoricalPerformance.objects.get_or_create(
            vendor=instance.vendor,
            date=instance.delivery_date.date(),
            defaults={
                'on_time_delivery_rate': instance.vendor.on_time_delivery_rate,
                'quality_rating_avg': quality_rating_avg,
                'average_response_time': instance.vendor.average_response_time,
                'fulfillment_rate': instance.vendor.fulfillment_rate,
            }
        )

        if not created:
            # Update existing HistoricalPerformance record
            historical_performance.quality_rating_avg = quality_rating_avg
            historical_performance.save()

# Average Response Time


@receiver(post_save, sender=PurchaseOrder)
def update_average_response_time(sender, instance, **kwargs):
    if instance.acknowledgment_date is not None:
        completed_orders = PurchaseOrder.objects.filter(vendor=instance.vendor, status="completed")
        response_times = completed_orders.exclude(acknowledgment_date__isnull=True).annotate(
            response_time=Func('acknowledgment_date', 'issue_date', function='TIMESTAMPDIFF', output_field=DurationField())
        ).aggregate(Avg('response_time'))['response_time__avg']

        # Update or create HistoricalPerformance record
        historical_performance, created = HistoricalPerformance.objects.get_or_create(
            vendor=instance.vendor,
            date=instance.delivery_date.date(),
            defaults={
                'on_time_delivery_rate': instance.vendor.on_time_delivery_rate,
                'quality_rating_avg': instance.vendor.quality_rating_avg,
                'average_response_time': response_times,
                'fulfillment_rate': instance.vendor.fulfillment_rate,
            }
        )

        if not created:
            # Update existing HistoricalPerformance record
            historical_performance.average_response_time = response_times
            historical_performance.save()

        print(f"Average Response Time updated for {instance.vendor.name}: {response_times}")


# Fulfilment Rate
@receiver(post_save, sender=PurchaseOrder)
@receiver(post_delete, sender=PurchaseOrder)
def update_fulfilment_rate(sender, instance, **kwargs):
    total_orders = PurchaseOrder.objects.filter(vendor=instance.vendor)
    completed_orders = total_orders.filter(status="completed", issue_date__lte=timezone.now())

    successful_orders = completed_orders.exclude(acknowledgment_date__isnull=True)

    total_count = total_orders.count()
    successful_count = successful_orders.count()

    fulfilment_rate = (successful_count / total_count) * 100 if total_count > 0 else 0

    # Update or create HistoricalPerformance record
    historical_performance, created = HistoricalPerformance.objects.get_or_create(
        vendor=instance.vendor,
        date=instance.delivery_date.date(),
        defaults={
            'on_time_delivery_rate': instance.vendor.on_time_delivery_rate,
            'quality_rating_avg': instance.vendor.quality_rating_avg,
            'average_response_time': instance.vendor.average_response_time,
            'fulfilment_rate': fulfilment_rate,
        }
    )

    if not created:
        # Update existing HistoricalPerformance record
        historical_performance.fulfilment_rate = fulfilment_rate
        historical_performance.save()

   
