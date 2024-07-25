from rest_framework import serializers
from .models import Price,Crypto

class PriceSerializer(serializers.ModelSerializer):
    """
    Serializer for the Price model to convert model instances into JSON format.
    """
    # Define the price field with a maximum of 30 digits and 4 decimal places.
    price = serializers.DecimalField(max_digits=30, decimal_places=4, coerce_to_string=False)
    
    # Define the symbol field, making it read-only and sourcing it from the related symbol field in the Price model.
    symbol = serializers.CharField(source='symbol.symbol', read_only=True)
    
    class Meta:
        """
        Meta class to specify the model and fields to exclude in the serializer.
        """
        model = Price
        # Exclude the "id" field from the serialized output.
        exclude = ("id",)
class CryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crypto
        exclude = ("id",)