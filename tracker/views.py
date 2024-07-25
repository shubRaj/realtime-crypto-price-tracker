from django.http import JsonResponse
from django.shortcuts import render
from .models import Price, Crypto
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import PriceSerializer,CryptoSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_livedata(request, symbol):
    """
    Retrieve live price data for a given cryptocurrency symbol.
    
    Args:
        request (HttpRequest): The HTTP request object.
        symbol (str): The symbol of the cryptocurrency.
        
    Returns:
        Response: JSON response containing the latest price data of the given cryptocurrency.
    """
    try:
        # Get the cryptocurrency object by symbol (case-insensitive).
        crypto = Crypto.objects.get(symbol__iexact=symbol)
    except get_object_or_404:
        # Return a JSON response with a 404 status code if the cryptocurrency is not found.
        return JsonResponse({
            "message": "Not Found"
        }, status=404)
    
    # Get the latest price for the cryptocurrency.
    price = Price.objects.filter(symbol=crypto).latest()
    
    # Serialize the price data.
    serializer = PriceSerializer(price)
    
    # Return the serialized data as a JSON response.
    return Response(serializer.data)

@api_view(['GET'])
def latest_day_data(request, symbol):
    """
    Retrieve the price data for the past 24 hours for a given cryptocurrency symbol.
    
    Args:
        request (HttpRequest): The HTTP request object.
        symbol (str): The symbol of the cryptocurrency.
        
    Returns:
        Response: JSON response containing the price data of the given cryptocurrency for the last 24 hours.
    """
    try:
        # Get the cryptocurrency object by symbol (case-insensitive).
        crypto = Crypto.objects.get(symbol__iexact=symbol)
    except get_object_or_404:
        # Return a JSON response with a 404 status code if the cryptocurrency is not found.
        return JsonResponse({
            "message": "Not Found"
        }, status=404)
    
    # Get the current time.
    now = timezone.now()
    
    # Calculate the time for the last 24 hours.
    last_24_hours = now - timedelta(hours=12)
    
    # Get the price data for the cryptocurrency created in the last 24 hours.
    prices = Price.objects.filter(symbol=crypto, created_at__gte=last_24_hours)
    
    # Serialize the price data.
    serializer = PriceSerializer(prices, many=True)
    
    # Return the serialized data as a JSON response.
    return Response(serializer.data)
@api_view(['GET'])
def get_symbols(request):
    serializer = CryptoSerializer(Crypto.objects.all(),many=True)
    return Response(serializer.data)
def home(request):
    return render(request,"tracker/index.html")