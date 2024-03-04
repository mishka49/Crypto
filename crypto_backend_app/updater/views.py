from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from updater.services import Updater


class UpdateView(APIView):
    def post(self, request):
        Updater.update()
        return Response(status=status.HTTP_200_OK)
