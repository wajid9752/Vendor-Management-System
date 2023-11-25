# To generate the token 
```
http://127.0.0.1:8000/api/vendors/
```

# To create the vendor 
```
Request : POST
http://127.0.0.1:8000/api/vendors/

<!-- Payload  -->
{
    "name": "",
    "contact_details": "1234567890",
    "address": "Delhi",
    "vendor_code": "ABC123",
    "on_time_delivery_rate": 95.5,
    "quality_rating_avg": 4.2,
    "average_response_time": 2.5,
    "fulfillment_rate": 98.0
}

```

# To Retrieve the list of vendors

```
Request: GET
http://127.0.0.1:8000/api/vendors/

```

# Retrieve a specific vendor's details.
```
Request: GET
http://127.0.0.1:8000/api/vendors/1/
```

# Update a vendor's details.

```
Request : PUT
http://127.0.0.1:8000/api/vendors/1/
<!-- Payload -->
{
    "name": "Rahul Singh",
    "contact_details": "8938019493",
    "address": "Delhi",
    "vendor_code": "ABC123",
    "on_time_delivery_rate": 95.5,
    "quality_rating_avg": 4.2,
    "average_response_time": 2.5,
    "fulfillment_rate": 98.0
}

```


# Delete a Vendor 
```
Request : DELETE
http://127.0.0.1:8000/api/vendors/1/
```



# Purchase Order


# Create a purchase order.

```
Request: POST
http://127.0.0.1:8000/api/purchase_orders/

<!-- Payload  -->

{
    "po_number": "PO123",
    "vendor": 1, 
    "order_date": "2023-11-30T12:00:00Z",
    "delivery_date": "2023-12-07T12:00:00Z",
    "items": [
        {
            "name": "Laptop Bag",
            "description": "Best Quanlity Item",
            "price": 200.0
        }
    ],
    "quantity": 10,
    "status": "Pending",
    "issue_date": "2023-11-28T12:00:00Z"
}


```

# List all purchase orders 
```
Request : GET
http://127.0.0.1:8000/api/purchase_orders/
```

# Retrieve details of a specific purchase order.
```
Request : GET
http://127.0.0.1:8000/api/purchase_orders/1/
```

# Update the Purchase Order
```
Request: PUT
http://127.0.0.1:8000/api/purchase_orders/1/


<!-- Payload -->
{
    "po_number": "PO123",
    "vendor": 1, 
    "order_date": "2023-11-30T12:00:00Z",
    "delivery_date": "2023-12-07T12:00:00Z",
    "items": [
        {
            "name": "Laptop Bags",
            "description": "Best Quanlity Item",
            "price": 200.0
        }
    ],
    "quantity": 10,
    "status": "Pending",
    "issue_date": "2023-11-28T12:00:00Z"
}


```


# Delete a purchase order.
```
Request : DELETE
http://127.0.0.1:8000/api/purchase_orders/1/
```




