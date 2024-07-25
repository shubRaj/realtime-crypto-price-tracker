from django.urls import path
from .views import latest_day_data, get_livedata,get_symbols,home

# Define the application namespace
app_name = "app_tracker"

# Define the URL patterns for the app
urlpatterns = [
    # URL pattern for retrieving live data for a given cryptocurrency symbol
    path("get-livedata/<str:symbol>/", get_livedata, name="get_live_data"),
    
    # URL pattern for retrieving the latest day data for a given cryptocurrency symbol
    path("latest-day-data/<str:symbol>/", latest_day_data, name="latest_day_data"),
    path("get-symbols/",get_symbols,name="get_symbols"),
    path("",home,name="home")
]
