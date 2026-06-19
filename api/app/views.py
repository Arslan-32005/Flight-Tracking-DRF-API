import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings

class RealTimeFlightsView(APIView):

    def get(self, request):

        api_key = settings.AVIATIONSTACK_API_KEY
        base_url = settings.AVIATIONSTACK_BASE_URL

        params = {
            "access_key": api_key,
            "dep_iata": request.query_params.get("dep_iata"),
            "arr_iata": request.query_params.get("arr_iata"),
            "limit": 10
        }
        
        response = requests.get(
            f"{base_url}/flights",
            params=params
        )

        return Response(response.json())