from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class WeatherDataView(APIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]  # Applying throttling

    def get(self, request, *args, **kwargs):
        # dummy weather data
        data = {
            "city": "Los Angeles",
            "temperature": "20°C",
            "condition": "Sunny",
        }
        return Response(data, status=200)
