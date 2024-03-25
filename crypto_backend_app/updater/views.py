import json

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from updater.services import UpdaterService, ExternalApiHandler


class UpdateView(APIView):
    def post(self, request):
        coins = ExternalApiHandler.get_coins()
        UpdaterService.update_coins(coins)
        return Response(status=status.HTTP_200_OK)
