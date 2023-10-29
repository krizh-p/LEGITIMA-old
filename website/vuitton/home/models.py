from django.db import models

# Create your models here.

class Token(models.Model):
    # Primary key field as a serialized token (CharField)
    token = models.CharField(max_length=40, primary_key=True)
    
    # Additional CharField
    data = models.CharField(max_length=1000000)

    def __str__(self):
        return self.token



# test has is "b323a95762617312ee59ce8f2e9b35757160881e"
# """{
#     "product_name": "Sample Product",
#     "product_id": "123456",
#     "manufacturer": "Sample Manufacturer",
#     "manufactured_date": "2023-10-25",
#     "sold_to_retailer_date": "2023-11-02",
#     "retailer": "Sample Retailer Inc.",
#     "price": 49.99,
#     "currency": "USD",
#     "category": "Electronics",
#     "color": "Black",
#     "weight": "1.2 kg",
#     "dimensions": {
#         "length": 10.5,
#         "width": 5.2,
#         "height": 2.0
#     },
#     "description": "This is a sample product description. It is a high-quality, feature-rich product suitable for various applications.",
#     "features": [
#         "Wireless connectivity",
#         "Long-lasting battery",
#         "HD display",
#         "Advanced functionality"
#     ],
#     "warranty": {
#         "valid_from": "2023-11-05",
#         "valid_to": "2024-11-05",
#         "warranty_provider": "Sample Warranty Services"
#     }
# }"""