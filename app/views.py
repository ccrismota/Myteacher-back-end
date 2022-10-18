from urllib import response
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

class HomeApiView(APIView):
    def get(self, request, format=None):
        return Response({"nome":"Cristiano", "idade": 35}, status=200)